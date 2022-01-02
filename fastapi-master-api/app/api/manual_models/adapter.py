from app.api.manual_models.adapter_enums import AdapterEnums
from app.api.models.adapter import Adapter


class AdapterManual(Adapter):
    adapter_name: AdapterEnums
