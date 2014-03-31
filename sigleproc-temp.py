import requests


def read_cities(file='./cities.txt'):
    with open(file, 'r') as f:
        cities = f.read().split('\n')
    return cities


def get(param):
    """Reduce number of parameters to the get method"""
    URL = 'http://api.openweathermap.org/data/2.5/weather'
    return requests.get(URL, params=param)


def main():
    """Main method"""
    cities = read_cities()
    params = [{'q': city, 'units': 'metric'} for city in cities]

    for param in params:
        r = get(param)
        try:
            json = r.json()
            print 'City: {city}, Temp: {temp} degrees'.format(
                city=json['name'], temp=json['main']['temp'])
        except:
            pass


if __name__ == '__main__':
    main()
