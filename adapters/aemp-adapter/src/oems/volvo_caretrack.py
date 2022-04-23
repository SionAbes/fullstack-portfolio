from src.oems.base_adapter import Adapter


class VolvoCaretrack(Adapter):
    def __init__(
        self,
        bootstrap_server: str,
        adapter_name: str,
        data_url: str,
        username: str,
        password: str,
    ):
        super().__init__(adapter_name, data_url, bootstrap_server)
        self.username = username
        self.password = password

    def _get_headers(self):
        from base64 import b64encode

        encoded_credentials = b64encode(
            bytes(f"{self.username}:{self.password}", encoding="ascii")
        ).decode("ascii")
        headers = {
            "Authorization": f"Basic {encoded_credentials}",
            "Content-Type": "application/json",
        }
        self.headers = headers

    def _parse_machine_header(self):
        self.aemp_machines = self.aemp_machines_raw
