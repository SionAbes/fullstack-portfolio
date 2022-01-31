from src.oems.base_adapter import Adapter


class LiebherrLidat(Adapter):
    def __init__(
        self,
        adapter_name: str,
        data_url: str,
        username: str,
        password: str,
    ):
        super().__init__(adapter_name, data_url)
        self.username = username
        self.password = password

    def _get_headers(self):
        from base64 import b64encode

        encoded_credentials = b64encode(
            bytes(f"{self.username}:{self.password}", encoding="ascii")
        ).decode("ascii")
        headers = {
            "Authorization": f"Basic {encoded_credentials}",
            "User-Agent": "PostmanRuntime/7.28.3",
        }
        self.headers = headers

    def _parse_machine_header(self):
        self.aemp_machines = self.aemp_machines_raw
