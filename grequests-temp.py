import grequests
import requests
from requests.adapters import HTTPAdapter

s = requests.Session()
s.mount('http://api.openweathermap.org/data/2.5/weather', HTTPAdapter(max_retries=5))

def read_cities(file='./cities.txt'):
    with open(file, 'r') as f:
        cities = f.read().split('\n')
    return cities


def print_res(r, *args, **kwargs):
    """Callback function that prints the result"""
    try:
        json = r.json()
        print 'City: {city}, Temp: {temp} degrees'.format(
            city=json['name'], temp=json['main']['temp'])
    except:
        pass


def get(params):
    """Reduce number of parameters to the get method"""
    URL = 'http://api.openweathermap.org/data/2.5/weather'
    for param in params:
        yield grequests.get(URL, params=param, session=s,
                            hooks=dict(response=print_res))


def main():
    """Main method"""
    cities = read_cities()
    params = [{'q': city, 'units': 'metric'} for city in cities]

    grequests.map(get(params), size=10)


if __name__ == '__main__':
    main()
