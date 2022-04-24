import json
from typing import List, Union

from app.domain.adapter import (
    Adapter,
    CreateVolvoCaretrackAdapter,
    CreateWackerNeusonKramerAdapter,
)
from app.repository.database.adapters import PolymorphicAdaptersBase, adapters_repo
from kafka import KafkaProducer
from sqlalchemy.orm import Session


class CreateAdapter:
    def __init__(
        self,
        db: Session,
        bootstrap_server: str,
        create_adapter: Union[
            CreateVolvoCaretrackAdapter, CreateWackerNeusonKramerAdapter
        ],
        adapters_repo: PolymorphicAdaptersBase = adapters_repo,
    ):
        self.db = db
        self.bootstrap_server = bootstrap_server
        self.create_adapter = create_adapter
        self.adapters_repo = adapters_repo

    def create(self) -> Adapter:
        adapter = self._create()
        self._send_create_message_to_kafka()
        return adapter

    def _create(self) -> Adapter:
        return self.adapters_repo.create(
            db=self.db,
            obj_in=self.create_adapter,
        )

    def _send_create_message_to_kafka(self):
        producer = KafkaProducer(
            bootstrap_servers=self.bootstrap_server,
            api_version=(0, 11, 5),
            value_serializer=lambda x: json.dumps(x).encode("utf-8"),
        )
        producer.send("adapter", {"status": "created"})


def fetch_adapters(
    *,
    db: Session,
) -> List[Adapter]:
    adapters = adapters_repo.list(db=db)
    return adapters
