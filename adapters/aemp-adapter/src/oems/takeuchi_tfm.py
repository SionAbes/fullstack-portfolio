from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session
from src.oems.base_adapter import Adapter


class TakeuchiTFM(Adapter):
    def __init__(
        self,
        adapter_name: str,
        data_url: str,
        token_url: str,
        client_id: str,
        client_secret: str,
    ):
        super().__init__(adapter_name, data_url)
        self.client_id = client_id
        self.token_url = token_url
        self.client_secret = client_secret

    def _get_headers(self):
        client = BackendApplicationClient(client_id=self.client_id)
        oauth = OAuth2Session(client=client, scope="api")
        token = oauth.fetch_token(
            token_url=self.token_url,
            client_id=self.client_id,
            client_secret=self.client_secret,
            include_client_id=True,
        )
        headers = {
            "Authorization": "Bearer {token}".format(token=token["access_token"]),
            "Content-Type": "application/json",
        }
        self.headers = headers

    def _parse_machine_header(self):
        self.aemp_machines = self.aemp_machines_raw
