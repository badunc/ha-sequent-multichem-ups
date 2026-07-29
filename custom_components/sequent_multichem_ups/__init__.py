"""The Sequent Multichemistry UPS integration."""

from __future__ import annotations

import logging

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)


async def async_setup(
    hass: HomeAssistant,
    config: dict,
) -> bool:
    """Set up the integration."""
    _LOGGER.info("Initializing Sequent Multichemistry UPS integration")

    hass.data.setdefault(DOMAIN, {})

    return True


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
) -> bool:
    """Set up from a config entry."""
    _LOGGER.info("Setting up config entry %s", entry.entry_id)

    return True


async def async_unload_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
) -> bool:
    """Unload the config entry."""
    _LOGGER.info("Unloading config entry %s", entry.entry_id)

    return True
