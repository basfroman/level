"""Dwelling module."""
import logging

from level.hub import Hub


class Dwelling:
    # all of existing dwellings
    _dwellings: list = []

    def __init__(self, title: str = None, description: str = None, location: str = None):
        self.title = title if title else f'Dwelling {len(self._dwellings)+ 1}'
        self.description = description
        self.location = location

        self._resident: str | None = None
        self._hub: Hub | None = None

        self._dwellings.append(self)

    @classmethod
    def create(cls, title: str = None, description: str = None, location: str = None):
        """Creates the dwelling in the collection."""
        dwelling = cls(title, description, location)
        logging.info(f'Dwelling "{dwelling.title}" successfully created.')
        return dwelling

    @classmethod
    def delete(cls, dwelling):
        """Removes dwelling from collection."""
        try:
            cls._dwellings.remove(dwelling)
            logging.info(f'Dwelling "{dwelling.title}" deleted successfully.')
        except ValueError:
            logging.info(f'Dwelling "{dwelling}" dos not exist.')

    @classmethod
    def all(cls):
        """Returns list of all dwellings from collection of by index."""
        return cls._dwellings

    def occupied(self, resident_name: str):
        """Occupies the dwelling."""
        if not self._resident:
            self._resident = resident_name
            logging.info(f'A new resident "{resident_name}" has moved into the dwelling "{self.title}".')
        else:
            logging.info(f'Dwelling {self.title} already occupied.')

    def vacant(self):
        """Makes the dwelling vacant."""
        logging.info(f'A resident no longer resides in the dwelling "{self.title}".')
        self._resident = None

    @property
    def resident(self) -> str | None:
        """Returns residents name."""
        return self._resident

    def install_hub(self, hub: Hub):
        """Installs hub to dwelling."""
        if not self._hub:
            self._hub = hub
            logging.info(f'Hub "{hub.title}" has been installed to the dwelling "{self.title}".')
        else:
            logging.info(f'Dwelling "{self.title}" has the hub "{self._hub.title}" already.')

    @property
    def hub(self):
        """Provides direct access to installed hub."""
        return self._hub

    def __repr__(self):
        """Returns the human-readable name of the dwelling."""
        return self.title
