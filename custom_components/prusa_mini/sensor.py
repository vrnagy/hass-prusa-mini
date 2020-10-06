"""Support for getting statistical data from a Prusa Mini 3D Printer."""

from . import PrusaMiniEntity
from .const import (
    DOMAIN,
    DATA_KEY_COORDINATOR,
    SENSOR_DICT,
    SENSOR_LIST,
)
from datetime import timedelta


async def async_setup_entry(hass, entry, async_add_entities):
    """Set up the Prusa Mini sensor."""
    data = hass.data[DOMAIN][entry.entry_id]

    sensors = [
        PrusaMiniSensor(
            data[DATA_KEY_COORDINATOR],
            entry.title,
            sensor_name,
            entry.entry_id,
        )
        for sensor_name in SENSOR_LIST
    ]
    async_add_entities(sensors, True)


class PrusaMiniSensor(PrusaMiniEntity):
    """Representation of a Prusa Mini sensor."""

    def __init__(self, coordinator, name, sensor_name, entity_id):
        """Initialize a Prusa Mini sensor."""
        super().__init__(coordinator, name, sensor_name, entity_id)

        variable_info = SENSOR_DICT[sensor_name]
        self._condition_name = variable_info[0]
        self._unit_of_measurement = variable_info[1]
        self._icon = variable_info[2]
        self._default = variable_info[3]

    @property
    def name(self):
        """Return the name of the sensor."""
        return f"{self._name} {self._condition_name}"

    @property
    def icon(self):
        """Icon to use in the frontend, if any."""

        func = getattr(self, f"{self._condition}_icon", None)
        if callable(func):
            return func(self.state)
        return self._icon

    @property
    def unit_of_measurement(self):
        """Return the unit the value is expressed in."""
        return self._unit_of_measurement

    @property
    def state(self):
        """Return the state of the device."""

        if (
            self.coordinator.data is not None
            and self._condition in self.coordinator.data
        ):
            state = self.coordinator.data[self._condition]
            func = getattr(self, self._condition, None)
            if callable(func):
                return func(state)
            return state

        return self._default

    def status_icon(self, state):
        if state == "Printing":
            return "mdi:printer-3d-nozzle"

        if state == "Idle":
            return "mdi:printer-3d-nozzle-outline"

        return "mdi:power-plug-off-outline"

    def time_est(self, state):
        """ Format Remaining Time """

        if state is None or state == "":
            return ""

        delta = timedelta(seconds=int(state))
        days = delta.days
        hours, remainder = divmod(delta.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        parts = []

        if days > 0:
            parts.append(f"{days}d")
        if hours > 0:
            parts.append(f"{hours}h")
        if minutes > 0:
            parts.append(f"{minutes}m")
        if seconds > 0:
            parts.append(f"{seconds}s")

        return " ".join(parts)