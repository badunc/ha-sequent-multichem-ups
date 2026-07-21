"""Driver for the Sequent Multichemistry UPS."""

from __future__ import annotations

import logging

from .const import DEFAULT_I2C_ADDRESS

_LOGGER = logging.getLogger(__name__)


class SequentUPS:
    """Represents a Sequent Multichemistry UPS."""

    def __init__(
        self,
        bus: int,
        address: int = DEFAULT_I2C_ADDRESS,
    ) -> None:
        """Initialize the driver."""
        self._bus = bus
        self._address = address

        _LOGGER.debug(
            "Driver initialized (bus=%s address=0x%02X)",
            bus,
            address,
        )

    @property
    def bus(self) -> int:
        """Return the I2C bus."""
        return self._bus

    @property
    def address(self) -> int:
        """Return the device address."""
        return self._address
