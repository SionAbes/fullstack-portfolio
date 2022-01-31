from oauthlib.oauth2 import LegacyApplicationClient
from requests_oauthlib import OAuth2Session
from src.oems.base_adapter import Adapter


class WackerNeusonKramerEquipcare(Adapter):
    def __init__(
        self,
        adapter_name: str,
        data_url: str,
        token_url: str,
        username: str,
        password: str,
        client_id: str,
        client_secret: str,
    ):
        super().__init__(adapter_name, data_url)
        self.token_url = token_url
        self.username = username
        self.password = password
        self.client_id = client_id
        self.client_secret = client_secret

    def _get_headers(self):
        client = LegacyApplicationClient(client_id=self.client_id)
        oauth = OAuth2Session(client=client, scope="api")
        token = oauth.fetch_token(
            token_url=self.token_url,
            client_id=self.client_id,
            client_secret=self.client_secret,
            username=self.username,
            password=self.password,
            include_client_id=True,
        )
        headers = {
            "Authorization": "Bearer {token}".format(token=token["access_token"]),
            "Content-Type": "application/json",
        }
        self.headers = headers

    def _parse_machine_header(self):
        self.aemp_machines = self.aemp_machines_raw
