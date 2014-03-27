import requests
from multiprocessing.dummy import Pool as ThreadPool


def main():
    """Main method"""

    cities = [
        'Chicago',
        'Houston',
        'Philadelphia',
        'Phoenix',
        'San Antonio',
        'San Diego',
        'Dallas',
        'San Jose',
        'Austin',
        'Jacksonville',
        'Indianapolis',
        'San Francisco',
        'Columbus',
        'Fort Worth',
        'Charlotte',
        'Detroit',
        'El Paso',
        'Memphis',
        'Boston',
        'Seattle',
        'Denver',
        'Washington',
        'Nashville-Davidson',
        'Baltimore',
        'Louisville-Jefferson County',
        'Portland',
        'Oklahoma City',
        'Milwaukee',
        'Las Vegas',
        'Albuquerque',
        'Tucson',
        'Fresno',
        'Sacramento',
        'Long Beach',
        'Kansas City',
        'Mesa',
        'Virginia Beach',
        'Atlanta',
        'Colorado Springs',
        'Raleigh',
        'Omaha',
        'Miami',
        'Oakland',
        'Tulsa',
        'Minneapolis',
        'Cleveland',
        'Wichita'
    ]

    params = [{'q': city, 'units': 'metric'} for city in cities]

    # Make the pool of workers
    pool = ThreadPool(10)

    results = pool.map(get, params)

    for r in results:
        json = r.json()
        print 'City: {city}, Temp: {temp} degrees'.format(
            city=json['name'], temp=json['main']['temp'])


def get(param):
    """Reduce number of parameters to the get method"""
    URL = 'http://api.openweathermap.org/data/2.5/weather'
    return requests.get(URL, params=param)


if __name__ == '__main__':
    main()
