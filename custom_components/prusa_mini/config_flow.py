"""Config flow to configure the Prusa Mini integration."""

from .const import DOMAIN  # pylint: disable=unused-import
from homeassistant import config_entries
from homeassistant.const import CONF_IP_ADDRESS
import ipaddress
import voluptuous as vol

DATA_SCHEMA = vol.Schema({vol.Required(CONF_IP_ADDRESS): str})


def ip_valid(host):
    """Return True if hostname or IP address is valid."""
    try:
        if ipaddress.ip_address(host).version == (4 or 6):
            return True
    except ValueError:
        return False


class PrusaMiniFlowHandler(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a Prusa Mini config flow."""

    VERSION = 1
    CONNECTION_CLASS = config_entries.CONN_CLASS_LOCAL_POLL

    async def async_step_user(self, user_input=None):
        """Handle a flow initiated by the user."""

        errors = {}

        if user_input is not None:
            ip_address = user_input.get(CONF_IP_ADDRESS)

            if ip_valid(ip_address):
                await self.async_set_unique_id(ip_address)
                self._abort_if_unique_id_configured()

                title = f"Prusa Mini {ip_address}"
                return self.async_create_entry(
                    title=title,
                    data={CONF_IP_ADDRESS: ip_address},
                )

            errors[CONF_IP_ADDRESS] = "invalid_ip"

        return self.async_show_form(
            step_id="user",
            data_schema=DATA_SCHEMA,
            errors=errors,
        )
