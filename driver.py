"""Driver module."""
from level import Dwelling
from level import Hub
from level.device import Switch
from level.device import Dimmer
from level.device import Lock
from level.device import Thermostat


def driver():
    # creates the Dwelling
    # way 1
    Dwelling.create('Apartment', 'Red house close the CVS.', '1234 El Camino Rd, Redwood City, CA')

    # way 2
    home = Dwelling.create('Home', 'My beautiful house.', '2000 Charleston Dr, Roseville, CA')
    print(f'All dwellings: {Dwelling.all()}')

    # getting Dwelling from the list
    first_home = Dwelling.all()[0]
    print(f'Resident at home: {first_home.resident}')
    # Dwelling - Occupied
    first_home.occupied('Roman Ch')
    print(f'Resident at home: {first_home.resident}')

    # Dwelling - Vacant
    first_home.vacant()
    print(f'Resident at home: {first_home.resident}')

    Dwelling.delete(first_home)
    print(f'All dwellings after deletion: {Dwelling.all()}')

    # create the HUB and install to the house.
    hub = Hub.create('home_hub')
    home.install_hub(hub)

    # Device - create the list of the devices
    devises = [
        Switch.create('Master Light'),
        Switch.create('Living Light'),
        Dimmer.create('Kitchen Light'),
        Dimmer.create('Hallway Light'),
        Lock.create('Entrance Lock'),
        Lock.create('Garage Side Lock'),
        Thermostat.create('Thermostat')
    ]
    for device in devises:
        hub.device_pair(device)
    print(f'All devices paired with hub "{hub}": {hub.devices()}')

    # THERMOSTATE
    thermostate = home.hub.devices()[6]
    print(f'Thermostate info: {thermostate.info()}')
    # please see the log
    thermostate.modify(target_temperature=64)
    print(f'Thermostate info after cooling: {thermostate.info()}')

    # DIMMER
    kitchen_light = home.hub.devices()[2]
    print('Kitchen switch info', kitchen_light.info())
    kitchen_light.turn_on()
    print('Kitchen switch info after turning on:', kitchen_light.info())
    kitchen_light.brightness(50)
    print('Kitchen switch info after brightness changes: ', kitchen_light.info())

    # LOCK
    entrance_lock = home.hub.devices()[4]
    print('Entrance lock info:', entrance_lock.info())
    entrance_lock.lock()
    entrance_lock.pin_set('1234')
    entrance_lock.unlock()
    print('Entrance lock info:', entrance_lock.info())
    entrance_lock.unlock(pin='123')
    print('Entrance lock info after enter wrong pin for unlock:', entrance_lock.info())
    entrance_lock.unlock(pin='1234')
    print('Entrance lock info:', entrance_lock.info())
    entrance_lock.modify()
    entrance_lock.modify()
    # removing the pin code
    entrance_lock.pin_change('1234', None)
    print('Entrance lock info:', entrance_lock.info())

    # SWITCH
    master_light = home.hub.devices()[0]
    print(f'Switch {master_light} info: {master_light.info()}')
    # changing the title of device
    master_light.title = 'Master LIGHT'
    print(f'Switch {master_light} info: {master_light.info()}')
    # please see the log
    master_light.turn_on()
    master_light.turn_off()
    master_light.modify()

    # Device - delete
    print('List of home hub devices:', home.hub.devices())
    # if we try to delete paired device then the error raised
    Switch.delete(master_light)

    # need to unpair this device
    home.hub.device_remove(master_light)
    # then delete
    Switch.delete(master_light)
    print('List of home hub devices:', home.hub.devices())


if __name__ == '__main__':
    driver()
