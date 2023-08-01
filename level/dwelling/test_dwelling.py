import unittest
from level import Dwelling
from level import Hub


class TestDwelling(unittest.TestCase):

    def setUp(self) -> None:
        self.home_title = 'test_home'
        self.home_description = 'test description'
        self.home_location = 'test location'

    def tearDown(self) -> None:
        Dwelling.all().clear()

    def test_create(self):
        """Test create method."""
        home = Dwelling(self.home_title, self.home_description, self.home_location)
        expected_home = Dwelling.all()[0]
        self.assertEqual(home, expected_home)

    def test_delete(self):
        home = Dwelling(self.home_title, self.home_description, self.home_location)
        Dwelling.delete(home)
        self.assertListEqual(Dwelling.all(), [])

    def test_all(self):
        for _ in range(5):
            Dwelling.create()
        self.assertEqual(len(Dwelling.all()), 5)

    def test_occupied(self):
        home = Dwelling(self.home_title, self.home_description, self.home_location)
        resident = 'Roman Ch'
        home.occupied(resident)
        self.assertEqual(home.resident, resident)

    def test_vacant(self):
        home = Dwelling(self.home_title, self.home_description, self.home_location)
        resident = 'Roman Ch'
        home.occupied(resident)
        home.vacant()
        self.assertIsNone(home.resident)

    def test_install_hub(self):
        home = Dwelling(self.home_title, self.home_description, self.home_location)
        hub = Hub('test_hub')
        home.install_hub(hub)
        self.assertEqual(home.hub, hub)


if __name__ == '__main__':
    unittest.main()

