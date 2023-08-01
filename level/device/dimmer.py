"""Dimmer class."""
import logging

from level.device.switch import Switch


class Dimmer(Switch):
    """Switch class."""

    def brightness(self, value: int):
        """Sets the brightness level from 0 to 100."""
        if 0 < value < 100:
            self._state = value
            logging.info(f'{self.__class__.__name__} "{self.title}" brightness has been set for {value}%.')
        else:
            logging.info('Brightness must be between 0 an 100.')
