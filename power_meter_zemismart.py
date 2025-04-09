"""SPM01_Zigbee_V2"""
"""TS0601_TZE284_iwn0gpzz"""

from zigpy.quirks.v2.homeassistant import (
    UnitOfElectricCurrent,
    UnitOfElectricPotential,
    UnitOfEnergy,
    UnitOfFrequency,
    UnitOfPower,
)
from zigpy.quirks.v2.homeassistant.sensor import SensorDeviceClass, SensorStateClass
import zigpy.types as t

from zhaquirks.tuya.builder import TuyaQuirkBuilder

(
    TuyaQuirkBuilder("_TZE284_iwn0gpzz", "TS0601")
    .tuya_sensor(
        dp_id=1,
        attribute_name="energy_consumed",
        fallback_name="Total energy consumed",
        type=t.uint16_t,
        state_class=SensorStateClass.TOTAL_INCREASING,
        device_class=SensorDeviceClass.ENERGY,
        unit=UnitOfEnergy.KILO_WATT_HOUR,
        divisor=100,
        translation_key="energy_consumed",
    )
    .tuya_sensor(
        dp_id=23,
        attribute_name="energy_produced",
        fallback_name="Total energy produced",
        type=t.uint16_t,
        state_class=SensorStateClass.TOTAL_INCREASING,
        device_class=SensorDeviceClass.ENERGY,
        unit=UnitOfEnergy.KILO_WATT_HOUR,
        divisor=100,
        translation_key="energy_produced",
    )
    .tuya_sensor(
        dp_id=111,
        attribute_name="total_active_power",
        fallback_name="total_active_power",
        type=t.uint16_t,
        state_class=SensorStateClass.MEASUREMENT,
        device_class=SensorDeviceClass.POWER,
        unit=UnitOfPower.WATT,
    )
    .tuya_sensor(
        dp_id=32,
        attribute_name="ac_frequency",
        fallback_name="ac_frequency",
        type=t.uint16_t,
        state_class=SensorStateClass.MEASUREMENT,
        device_class=SensorDeviceClass.FREQUENCY,
        unit=UnitOfFrequency.HERTZ,
        divisor=100,
    
    )
    .tuya_sensor(
        dp_id=50,
        attribute_name="power_factor",
        fallback_name="power_factor",
        type=t.uint16_t,
        state_class=SensorStateClass.MEASUREMENT,
        device_class=SensorDeviceClass.POWER_FACTOR,
        divisor=100,
    )
    .tuya_sensor(
        dp_id=102,
        attribute_name="voltage_phase",
        fallback_name="voltage_phase",
        type=t.uint16_t,
        state_class=SensorStateClass.MEASUREMENT,
        device_class=SensorDeviceClass.VOLTAGE,
        divisor=10,
        unit=UnitOfElectricPotential.VOLT,
    )
    .tuya_sensor(
        dp_id=103,
        attribute_name="current_phase",
        translation_key="current_phase",
        fallback_name="Current (phase A)",
        type=t.uint16_t,
        state_class=SensorStateClass.MEASUREMENT,
        device_class=SensorDeviceClass.CURRENT,
        divisor=1000,
        unit=UnitOfElectricCurrent.AMPERE,
    )
    .tuya_sensor(
        dp_id=104,
        attribute_name="power_phase",
        fallback_name="power_phase",
        type=t.uint16_t,
        state_class=SensorStateClass.MEASUREMENT,
        device_class=SensorDeviceClass.POWER,
        unit=UnitOfPower.WATT,
    )

    .add_to_registry()
)