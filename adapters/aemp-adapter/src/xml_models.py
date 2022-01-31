from dataclasses import dataclass, field
from typing import List, Optional

AEMP_METRICS = (
    "cumulative_operating_hours",
    "distance",
    "cumulative_idle_hours",
    "fuel_remaining",
    "fuel_used",
    "def_remaining",
    "cumulative_power_take_off_hours",
    "average_daily_load_factor_last_24",
    "maximum_speed_last_24",
    "cumulative_load_count",
    "cumulative_payload_totals",
    "cumulative_active_regeneration_hours",
    "cumulative_non_productive_idle_hours",
    "fuel_used_last_24",
    "cumulative_idle_non_operating_hours",
)


@dataclass
class EquipmentHeader:
    """
    See section 11.2 of ISO/TS 15143-3:2016
    """

    class Meta:
        name = "EquipmentHeader"

    unit_install_date_time: Optional[str] = field(
        default=None,
        metadata=dict(name="UnitInstallDateTime"),
    )
    oem_name: Optional[str] = field(
        default=None,
        metadata=dict(name="OEMName"),
    )
    model: Optional[str] = field(default=None, metadata=dict(name="Model"))
    make: Optional[str] = field(default=None, metadata=dict(name="Make"))
    equipment_id: Optional[str] = field(
        default=None,
        metadata=dict(name="EquipmentID"),
    )
    serial_number: Optional[str] = field(
        default=None,
        metadata=dict(name="SerialNumber"),
    )
    pin: Optional[str] = field(default=None, metadata=dict(name="PIN"))


@dataclass
class Location:
    """
    See section 11.3 of ISO/TS 15143-3:2016
    """

    class Meta:
        name = "Location"

    datetime: str = field(
        default=None,
        metadata=dict(type="Attribute", name="datetime"),
    )
    latitude: float = field(
        default=None,
        metadata=dict(name="Latitude", type="Element"),
    )
    longitude: float = field(
        default=None,
        metadata=dict(name="Longitude", type="Element"),
    )
    altitude: float = field(
        default=None,
        metadata=dict(name="Altitude", type="Element"),
    )
    altitude_units: str = field(
        default=None,
        metadata=dict(name="AltitudeUnits", type="Element"),
    )


@dataclass
class CumulativeOperatingHours:
    class Meta:
        name = "CumulativeOperatingHours"

    datetime: str = field(
        default=None,
        metadata=dict(type="Attribute", name="datetime"),
    )
    hour: str = field(
        default=None,
        metadata=dict(name="Hour", type="Element"),
    )


@dataclass
class FuelUsed:
    """
    Amount of fuel consumed by the machine
    """

    class Meta:
        name = "FuelUsed"

    datetime: str = field(
        default=None,
        metadata=dict(type="Attribute", name="datetime"),
    )
    fuel_units: str = field(
        default=None,
        metadata=dict(name="FuelUnits", type="Element"),
    )
    fuel_consumed: float = field(
        default=None,
        metadata=dict(name="FuelConsumed", type="Element"),
    )


@dataclass
class FuelUsedLast24:
    """
    Amount of fuel consumed by the machine
    """

    class Meta:
        name = "FuelUsedLast24"

    datetime: str = field(
        default=None,
        metadata=dict(type="Attribute", name="datetime"),
    )
    fuel_units: str = field(
        default=None,
        metadata=dict(name="FuelUnits", type="Element"),
    )
    fuel_consumed: float = field(
        default=None,
        metadata=dict(name="FuelConsumed", type="Element"),
    )


@dataclass
class Distance:
    """
    Distance travelled
    """

    class Meta:
        name = "Distance"

    datetime: str = field(
        default=None,
        metadata=dict(type="Attribute", name="datetime"),
    )
    odometer_units: str = field(
        default=None,
        metadata=dict(name="OdometerUnits", type="Element"),
    )
    odometer: float = field(
        default=None,
        metadata=dict(name="Odometer", type="Element"),
    )


@dataclass
class CumulativeIdleHours:
    class Meta:
        name = "CumulativeIdleHours"

    datetime: str = field(
        default=None,
        metadata=dict(type="Attribute", name="datetime"),
    )
    hour: float = field(default=None, metadata=dict(name="Hour", type="Element"))


@dataclass
class FuelRemaining:
    class Meta:
        name = "FuelRemaining"

    datetime: str = field(
        default=None,
        metadata=dict(type="Attribute", name="datetime"),
    )
    percent: float = field(
        default=None,
        metadata=dict(name="Percent", type="Element"),
    )
    fuel_tank_capacity_units: str = field(
        default=None,
        metadata=dict(name="FuelTankCapacityUnits", type="Element"),
    )
    fuel_tank_capacity: float = field(
        default=None,
        metadata=dict(name="FuelTankCapacity", type="Element"),
    )


@dataclass
class DEFRemaining:
    class Meta:
        name = "DEFRemaining"

    datetime: str = field(
        default=None,
        metadata=dict(type="Attribute", name="datetime"),
    )
    percent: float = field(
        default=None,
        metadata=dict(name="Percent", type="Element"),
    )
    def_tank_capacity_units: str = field(
        default=None,
        metadata=dict(name="DEFTankCapacityUnits", type="Element"),
    )
    def_tank_capacity: float = field(
        default=None,
        metadata=dict(name="DEFTankCapacity", type="Element"),
    )


@dataclass
class EngineStatus:
    class Meta:
        name = "EngineStatus"

    datetime: str = field(
        default=None,
        metadata=dict(type="Attribute", name="datetime"),
    )
    engine_number: float = field(
        default=None,
        metadata=dict(name="EngineNumber", type="Element"),
    )
    running: bool = field(
        default=None,
        metadata=dict(name="Running", type="Element"),
    )


@dataclass
class CumulativePowerTakeOffHours:
    class Meta:
        name = "CumulativePowerTakeOffHours"

    datetime: str = field(
        default=None,
        metadata=dict(type="Attribute", name="datetime"),
    )
    hour: float = field(default=None, metadata=dict(name="Hour", type="Element"))


@dataclass
class AverageDailyLoadFactorLast24:
    class Meta:
        name = "AverageDailyLoadFactorLast24"

    datetime: str = field(
        default=None,
        metadata=dict(type="Attribute", name="datetime"),
    )
    load_factor: float = field(
        default=None,
        metadata=dict(name="LoadFactor", type="Element"),
    )


@dataclass
class MaximumSpeedLast24:
    class Meta:
        name = "MaximumSpeedLast24"

    datetime: str = field(
        default=None,
        metadata=dict(type="Attribute", name="datetime"),
    )
    speed_units: str = field(
        default=None,
        metadata=dict(name="SpeedUnits", type="Element"),
    )
    speed: float = field(default=None, metadata=dict(name="Speed", type="Element"))


@dataclass
class CumulativeLoadCount:
    class Meta:
        name = "CumulativeLoadCount"

    datetime: str = field(
        default=None,
        metadata=dict(type="Attribute", name="datetime"),
    )
    count: float = field(default=None, metadata=dict(name="Count", type="Element"))


@dataclass
class CumulativePayloadTotals:
    class Meta:
        name = "CumulativePayloadTotals"

    datetime: str = field(
        default=None,
        metadata=dict(type="Attribute", name="datetime"),
    )
    weight_unit: str = field(
        default=None,
        metadata=dict(name="WeightUnit", type="Element"),
    )
    payload: float = field(
        default=None,
        metadata=dict(name="Payload", type="Element"),
    )


@dataclass
class CumulativeActiveRegenerationHours:
    class Meta:
        name = "CumulativeActiveRegenerationHours"

    datetime: str = field(
        default=None,
        metadata=dict(type="Attribute", name="datetime"),
    )
    hour: float = field(default=None, metadata=dict(name="Hour", type="Element"))


@dataclass
class CumulativeNonProductiveIdleHours:
    class Meta:
        name = "CumulativeNonProductiveIdleHours"

    datetime: str = field(
        default=None,
        metadata=dict(type="Attribute", name="datetime"),
    )
    hour: float = field(default=None, metadata=dict(name="Hour", type="Element"))


@dataclass
class CumulativeIdleNonOperatingHours:
    class Meta:
        name = "CumulativeIdleNonOperatingHours"

    datetime: str = field(
        default=None,
        metadata=dict(type="Attribute", name="datetime"),
    )
    hour: float = field(default=None, metadata=dict(name="Hour", type="Element"))


@dataclass
class Equipment:
    class Meta:
        name = "Equipment"

    equipment_header: EquipmentHeader = field(
        default=None,
        metadata=dict(name="EquipmentHeader"),
    )
    location: Optional[Location] = field(
        default=None,
        metadata=dict(name="Location"),
    )
    cumulative_operating_hours: Optional[CumulativeOperatingHours] = field(
        default=None,
        metadata=dict(name="CumulativeOperatingHours"),
    )
    fuel_used: Optional[FuelUsed] = field(
        default=None,
        metadata=dict(name="FuelUsed", required=False),
    )
    distance: Optional[Distance] = field(
        default=None,
        metadata=dict(name="Distance", required=False),
    )
    cumulative_idle_hours: Optional[CumulativeIdleHours] = field(
        default=None,
        metadata=dict(
            name="CumulativeIdleHours",
            required=False,
        ),
    )
    fuel_remaining: Optional[FuelRemaining] = field(
        default=None,
        metadata=dict(name="FuelRemaining", required=False),
    )
    def_remaining: Optional[DEFRemaining] = field(
        default=None,
        metadata=dict(name="DEFRemaining", required=False),
    )
    engine_status: Optional[EngineStatus] = field(
        default=None,
        metadata=dict(name="EngineStatus", required=False),
    )
    cumulative_power_take_off_hours: Optional[CumulativePowerTakeOffHours] = field(
        default=None,
        metadata=dict(
            name="CumulativePowerTakeOffHours",
            required=False,
        ),
    )
    average_daily_load_factor_last_24: Optional[AverageDailyLoadFactorLast24] = field(
        default=None,
        metadata=dict(
            name="AverageDailyLoadFactorLast24",
            required=False,
        ),
    )
    maximum_speed_last_24: Optional[MaximumSpeedLast24] = field(
        default=None,
        metadata=dict(
            name="MaximumSpeedLast24",
            required=False,
        ),
    )
    cumulative_load_count: Optional[CumulativeLoadCount] = field(
        default=None,
        metadata=dict(
            name="CumulativeLoadCount",
            required=False,
        ),
    )
    cumulative_payload_totals: Optional[CumulativePayloadTotals] = field(
        default=None,
        metadata=dict(
            name="CumulativePayloadTotals",
            required=False,
        ),
    )
    cumulative_active_regeneration_hours: Optional[
        CumulativeActiveRegenerationHours
    ] = field(
        default=None,
        metadata=dict(
            name="CumulativeActiveRegenerationHours",
            required=False,
        ),
    )
    cumulative_non_productive_idle_hours: Optional[
        CumulativeNonProductiveIdleHours
    ] = field(
        default=None,
        metadata=dict(
            name="CumulativeNonProductiveIdleHours",
            required=False,
        ),
    )
    cumulative_idle_non_operating_hours: Optional[
        CumulativeIdleNonOperatingHours
    ] = field(
        default=None,
        metadata=dict(
            name="CumulativeIdleNonOperatingHours",
            required=False,
        ),
    )
    fuel_used_last_24: Optional[FuelUsedLast24] = field(
        default=None,
        metadata=dict(
            name="FuelUsedLast24",
            required=False,
        ),
    )


@dataclass
class Links:
    """
    Links to the current, previous, next and last pages will be provided for easy navigation
    See section 7 of ISO/TS 15143-3:2016
    """

    class Meta:
        name = "Links"

    relation: str = field(metadata=dict(name="rel"))
    hypertext_reference: str = field(metadata=dict(name="href"))


@dataclass
class Fleet:
    class Meta:
        name = "Fleet"

    links: List[Links] = field(
        default_factory=list,
        metadata=dict(name="Links"),
    )
    equipment: List[Equipment] = field(
        default_factory=list,
        metadata=dict(name="Equipment"),
    )
