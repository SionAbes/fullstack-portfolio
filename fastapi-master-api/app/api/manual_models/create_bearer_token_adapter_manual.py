from app.api.manual_models.adapter_enums import AdapterEnums
from app.api.models.create_bearer_token_adapter import CreateBearerTokenAdapter


class CreateBearerTokenAdapterManual(CreateBearerTokenAdapter):
    adapter_name: AdapterEnums
