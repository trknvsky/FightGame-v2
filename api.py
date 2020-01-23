import requests

APP_ID = 'AIzaSyChw-V04qU5R705zAeHGAP6wXkofZGpy80'
URL = 'https://maps.googleapis.com/maps/api/geocode/json'


class GeocodeAPi:

    def get_cords_by_location(self, location):
        response = requests.get(URL, {
            'key': APP_ID,
            'address': location
        })
        if response.json()['status'] == 'OK':
            results = response.json()['results'][0]
            coords = results['geometry']['location']
            print('location {}:'.format(location), coords)
        return coords
