"""Base device module."""
import abc
import logging

from level.errors import DeviceError


class BaseDevice:
    """Base device class."""
    # all created devices
    _devices = []
    _state = 0

    def __init__(self, title=None):
        self.title = title if title else f'{self.__class__.__name__} {len(self._devices) + 1}'
        self._paired = False
        self._devices.append(self)
        logging.info(f'{self.__class__.__name__} "{self.title}" has been created.')

    @classmethod
    def create(cls, title: str | None = None):
        """Creates the device in the devices' collection."""
        return cls(title)

    @classmethod
    def delete(cls, device):
        if isinstance(device, cls) and device.paired:
            logging.info(f'{cls.__name__} "{device.title}" cannot be deleted.')
        else:
            cls._devices.remove(device)
            logging.info(f'{cls.__name__} "{device.title}" has been deleted.')

    @abc.abstractmethod
    def info(self):
        """Abstract method gets device status of class instance."""

    @abc.abstractmethod
    def modify(self, *args, **kwargs):
        """Abstract method for changing device status of class instance."""

    @classmethod
    def all(cls):
        """Returns all devises."""
        return cls._devices

    @property
    def paired(self):
        """Returns paired state of device."""
        return self._paired

    @paired.setter
    def paired(self, value: bool):
        """Changes the paired state of device."""
        self._paired = value

    def __repr__(self):
        """Returns the human-readable name of the device."""
        return f'{self.__class__.__name__} <{self.title}>'
