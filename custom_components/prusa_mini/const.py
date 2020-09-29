"""Constants of the Prusa Mini component."""

from datetime import timedelta

from homeassistant.const import PERCENTAGE, TEMP_CELSIUS

DOMAIN = "prusa_mini"

DATA_KEY_COORDINATOR = "coordinator"

MIN_TIME_BETWEEN_UPDATES = timedelta(seconds=15)

SENSOR_DICT = {
    "status": ["Status", "", None, "Off"],
    "temp_nozzle": ["Nozzle Temp", TEMP_CELSIUS, None, 0],
    "temp_bed": ["Bed Temp", TEMP_CELSIUS, None, 0],
    "progress": ["Progress", PERCENTAGE, "mdi:file-percent", 0],
    "material": ["Material", "", "mdi:printer-3d", ""],
    "project_name": ["File", "", "mdi:file-code", ""],
    "print_dur": ["Time Elapsed", "", "mdi:clock-time-four", ""],
    "time_est": ["Time Remaining", "", "mdi:clock-time-four", ""],
    "flow_factor": ["Flow Rate", PERCENTAGE, "mdi:filter-variant", 0],
    "printing_speed": ["Printing Speed", PERCENTAGE, "mdi:speedometer", 0],
    "pos_z_mm": ["Z Height", "mm", "mdi:ruler-square", 0],
}

SENSOR_LIST = list(SENSOR_DICT)