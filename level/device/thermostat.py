"""Thermostat module."""
import logging

from level.device.base import BaseDevice

STOPPED = 0
HEATING = 1
COOLING = 2


class Thermostat(BaseDevice):
    # in the real live the thermostat gets this from sensor
    _current_temperature: int = 72
    _target_temperature: int | None = None

    def heating(self, target_temperature):
        """Heating the dwelling until the temperature."""
        self._state = HEATING
        self._target_temperature = target_temperature
        logging.info(f'Thermostat heats up to {target_temperature} degrees.')
        while target_temperature > self._current_temperature:
            # heating the dwelling
            self._current_temperature += 1
            logging.info(f'The dwelling temperature is {self._current_temperature} degree.')
        self._state = STOPPED

    def cooling(self, target_temperature):
        """Cooling the dwelling until the temperature."""
        self._state = COOLING
        self._target_temperature = target_temperature
        logging.info(f'Thermostat cools down to {target_temperature} degrees.')
        while target_temperature < self._current_temperature:
            # heating the dwelling
            self._current_temperature -= 1
            logging.info(f'The dwelling temperature is {self._current_temperature} degree.')
        self._state = STOPPED

    def info(self):
        """Returns state of the device."""
        return {
            'device': self.__class__.__name__.lower(),
            'state': self._state,
            'temperature': {
                'current': self._current_temperature,
                'temperature set': self._target_temperature}}

    def modify(self, target_temperature: int | None):
        """Changes the state of the thermostate"""
        if target_temperature > self._current_temperature:
            self.heating(target_temperature)
        else:
            self.cooling(target_temperature)
