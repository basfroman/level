"""Hub module."""
import logging

from level.device.base import BaseDevice
from level.errors import HubError


class Hub:
    _hubs = []
    _devices = []

    def __init__(self, title: str | None = None):
        self.title = title if title else f'Hub {len(self._hubs) + 1}'

    @classmethod
    def create(cls, title: str = None):
        """Creates the hub in the collection."""
        hub = cls(title)
        logging.info(f'Hub "{hub.title}" successfully created.')
        return hub

    def device_pair(self, device: BaseDevice):
        """Pairs the device."""
        if not device.paired:
            self._devices.append(device)
            device.paired = True
            logging.info(f'{device.__class__.__name__} "{device.title}" successfully paired to hub "{self.title}".')

    def device_state(self, device: BaseDevice):
        """Get device state."""
        return device.info()

    def devices(self) -> list[BaseDevice]:
        """Gets list of all paired devices."""
        return self._devices

    def device_remove(self, device: BaseDevice):
        """Remove device from hub."""
        if device in self._devices:
            self._devices.remove(device)
            device.paired = False
            logging.info(f'{device.__class__.__name__} "{device.title}" was deleted from hub "{self.title}".')
        else:
            logging.info(f'{device.__class__.__name__} "{device.title}" was not paired with hub "{self.title}".')

    def __repr__(self):
        """Returns the human-readable name of the dwelling."""
        return self.title
