from game import *
from api import *


def main():
    fight = Fight()
    geocode_api = GeocodeAPi()
    location = input('Input location: ')
    geocode_api.get_cords_by_location(location)
    fight.play()


if __name__ == '__main__':
    main()
