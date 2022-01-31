import datetime
import json
from dataclasses import asdict
from typing import List

import requests
from lxml import etree
from src.xml_models import AEMP_METRICS, Fleet
from xsdata.formats.dataclass.parsers.xml import XmlParser


class Adapter:
    def __init__(self, adapter_name: str, data_url: str):
        self.adapter_name = adapter_name
        self.data_url = data_url
        self.headers = None
        self.aemp_machines_raw = None
        self.aemp_machines = None

    def __call__(self, *args, **kwargs):
        self._get_headers()
        self._get_aemp_snapshot_machines()
        self._parse_machine_header()
        messages = self._create_metric_messages()
        self._save_to_file(messages=messages)

    def _get_headers(self):
        ...

    def _parse_machine_header(self):
        ...

    def _get_aemp_snapshot_machines(self):
        requests_session = requests.session()
        requests_session.headers.update(self.headers)

        this_page = self.data_url
        next_page = self.data_url
        last_page = None
        aemp_machines_raw = []
        while this_page != last_page:
            this_page = next_page
            try:
                response = requests_session.get(url=this_page, data={})
                response.raise_for_status()
                xml_response = response.content
                root = etree.fromstring(xml_response)
                for elem in root.getiterator():
                    elem.tag = etree.QName(elem).localname
                etree.cleanup_namespaces(root)

                obj = XmlParser().from_bytes(etree.tostring(root), Fleet)
                obj_as_dict = asdict(obj)
                aemp_machines_raw.extend(obj_as_dict["equipment"])
                if obj.links:
                    for link in obj.links:
                        if link.relation == "next":
                            next_page = link.hypertext_reference
                        if link.relation == "last":
                            last_page = link.hypertext_reference
                else:
                    last_page = this_page
            except requests.exceptions.HTTPError as err:
                raise SystemExit(err)
        self.aemp_machines_raw = aemp_machines_raw

    def _create_metric_messages(self) -> List:
        machine_metrics = []
        for machine in self.aemp_machines:
            processing_datetime = datetime.datetime.utcnow().isoformat()
            for metric in AEMP_METRICS:
                metric_data = machine.get(metric)
                if not metric_data:
                    continue
                timestamp = metric_data.pop("datetime", None)
                if timestamp is None or timestamp == "":
                    continue

                for field_name, value in metric_data.items():
                    if field_name == "percent":
                        unit = "%"
                        metric_data = {field_name: value}
                        break
                    elif "units" in field_name:
                        unit = value
                        metric_data.pop(field_name, None)
                        break
                    elif field_name is None:
                        unit = ""
                    else:
                        unit = field_name

                for field_name, value in metric_data.items():
                    if value:
                        machine_metrics.append(
                            {
                                "processing_datetime": processing_datetime,
                                "event_time": timestamp,
                                "machine": machine["equipment_header"],
                                "oem": self.adapter_name,
                                "metric": "{}".format(metric),
                                "value": float(value),
                                "unit": unit,
                            }
                        )

            # prepare location metric
            if machine.get("location"):
                event_time = machine["location"]["datetime"]
                if event_time is None or event_time == "":
                    continue
                machine_metrics.append(
                    {
                        "processing_datetime": processing_datetime,
                        "event_time": event_time,
                        "machine": machine["equipment_header"],
                        "oem": self.adapter_name,
                        "metric": "location",
                        "value": {
                            "type": "Point",
                            "coordinates": [
                                machine["location"]["longitude"],
                                machine["location"]["latitude"],
                            ],
                            "altitude": machine["location"].get("altitude"),
                        },
                    }
                )
        return machine_metrics

    def _save_to_file(self, messages: List):
        date_time = datetime.datetime.utcnow().strftime("%d-%m-%Y--%H-%M-%S")
        with open(f"./data/{self.adapter_name}/{date_time}.json", "w") as f:
            json.dump(messages, f)
