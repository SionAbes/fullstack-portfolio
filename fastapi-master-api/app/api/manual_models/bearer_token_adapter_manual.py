from app.api.manual_models.adapter_enums import AdapterEnums
from app.api.models.bearer_token_adapter import BearerTokenAdapter


class BearerTokenAdapterManual(BearerTokenAdapter):
    adapter_name: AdapterEnums
