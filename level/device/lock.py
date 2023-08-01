"""Lock module."""
import logging

from level.device.base import BaseDevice

UNLOCKED = 0
LOCKED = 1


class Lock(BaseDevice):

    _pin: str | None = None

    def lock(self):
        """Locks the lock."""
        self._state = LOCKED
        logging.info(f'Lock "{self.title}" locked.')

    def unlock(self, pin: str | None = None):
        """Unlocks the lock."""
        if pin != self._pin:
            logging.info('Wrong pin code. Please provide the pin code.')
            return
        self._state = UNLOCKED
        logging.info(f'Lock "{self.title}" unlocked.')

    def info(self):
        """Returns state of the lock."""
        return {'device': self.__class__.__name__.lower(), 'state': self._state, 'pin code': self._pin is not None}

    def modify(self, *args, **kwargs):
        if self._state == UNLOCKED:
            self.lock()
        else:
            self.unlock(*args, **kwargs)

    def pin_set(self, pin: str):
        """Sets pin to the lock."""
        if self._pin:
            logging.info(f'Lock "{self.title}" already has a pin code.')
        else:
            self._pin = pin
            logging.info(f'Pin code for lock "{self.title}" is set.')

    def pin_change(self, old_pin: str, new_pin: str | None):
        """Changes the pin for lock."""
        if self._pin == old_pin:
            self._pin = new_pin
            logging.info(f'Pin code for lock {self.title} {"is changed" if new_pin else "removed"}.')
        else:
            logging.info(f'Wrong old pin code for lock {self.title}.')
