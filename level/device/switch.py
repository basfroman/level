"""Switch module."""
import logging

from level.device.base import BaseDevice


class Switch(BaseDevice):

    def turn_on(self):
        """Turns on the switch."""
        self._state = 100
        logging.info(f'{self.__class__.__name__} "{self.title}" turned on.')

    def turn_off(self):
        """Turns off the switch."""
        self._state = 0
        logging.info(f'{self.__class__.__name__} "{self.title}" turned off.')

    def info(self):
        """Returns state of the device."""
        return {'device': self.__class__.__name__.lower(), 'state': self._state}

    def modify(self):
        """Changes the state of the switch"""
        if self._state:
            self.turn_off()
        else:
            self.turn_on()
