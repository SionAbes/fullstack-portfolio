from app.api.manual_models.adapter_enums import AdapterEnums
from app.api.models.create_adapter import CreateAdapter


class CreateAdapterManual(CreateAdapter):
    adapter_name: AdapterEnums
