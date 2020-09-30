"""Prusa Mini sensor integration."""

import logging

from aiohttp import ClientTimeout
from .const import DOMAIN, DATA_KEY_COORDINATOR, MIN_TIME_BETWEEN_UPDATES
from homeassistant.config_entries import SOURCE_IMPORT
from homeassistant.const import CONF_IP_ADDRESS
from homeassistant.helpers.update_coordinator import (
    CoordinatorEntity,
    DataUpdateCoordinator,
    UpdateFailed,
)
from homeassistant.helpers.aiohttp_client import async_get_clientsession

_LOGGER = logging.getLogger(__name__)


async def async_setup(hass, config):
    """Set up the Prusa Mini integration."""

    hass.data[DOMAIN] = {}

    if DOMAIN in config:
        for entry_config in config[DOMAIN]:
            hass.async_create_task(
                hass.config_entries.flow.async_init(
                    DOMAIN, context={"source": SOURCE_IMPORT}, data=entry_config
                )
            )

    return True


async def async_setup_entry(hass, entry):
    """Set up the Prusa Mini platform."""

    session = async_get_clientsession(hass)

    async def async_update_data():
        """Fetch data from API endpoint."""
        try:
            async with session.get(
                f"http://{entry.data[CONF_IP_ADDRESS]}/api/telemetry",
                timeout=ClientTimeout(total=5),
            ) as resp:
                json = await resp.json()
                if "project_name" in json:
                    json["status"] = "Printing"
                else:
                    json["status"] = "Idle"

                if "print_dur" in json:
                    json["print_dur"].strip()

                return json

        except Exception:  # pylint: disable=broad-except
            return {
                "status": "Off",
            }

    coordinator = DataUpdateCoordinator(
        hass,
        _LOGGER,
        name=entry.title,
        update_method=async_update_data,
        update_interval=MIN_TIME_BETWEEN_UPDATES,
    )

    hass.data[DOMAIN][entry.entry_id] = {
        DATA_KEY_COORDINATOR: coordinator,
    }

    await coordinator.async_refresh()

    hass.async_create_task(
        hass.config_entries.async_forward_entry_setup(entry, "sensor")
    )

    return True


class PrusaMiniEntity(CoordinatorEntity):
    """Representation of a Prusa Mini entity."""

    def __init__(self, coordinator, name, sensor_name, entity_id):
        """Initialize a Prusa Mini entity."""
        super().__init__(coordinator)
        self._name = name
        self._entity_id = entity_id
        self._condition = sensor_name
        self._unique_id = f"{entity_id}_{sensor_name}"

    @property
    def icon(self):
        """Icon to use in the frontend, if any."""
        return "mdi:printer-3d"

    @property
    def unique_id(self) -> str:
        """Return a unique ID."""
        return self._unique_id

    @property
    def device_info(self):
        """Return the device information of the entity."""
        return {
            "identifiers": {(DOMAIN, self._entity_id)},
            "name": self._name,
            "manufacturer": "Prusa",
            "model": "MINI",
        }