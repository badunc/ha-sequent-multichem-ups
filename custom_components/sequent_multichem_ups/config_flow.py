"""Config flow for the Sequent Multichemistry UPS integration."""

from __future__ import annotations

from homeassistant import config_entries

from .const import DOMAIN


class SequentUPSConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for the Sequent Multichemistry UPS."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""

        if user_input is not None:
            await self.async_set_unique_id("sequent_multichem_ups")
            self._abort_if_unique_id_configured()

            return self.async_create_entry(
                title="Sequent Multichemistry UPS",
                data={},
            )

        return self.async_show_form(
            step_id="user",
            data_schema=None,
        )