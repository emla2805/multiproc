import grequests
import requests
from requests.adapters import HTTPAdapter

s = requests.Session()
s.mount('http://www.telize.com/geoip/', HTTPAdapter(max_retries=5))

def read_ips(file='./ips.txt'):
    """Read ips from file and return a list"""
    with open(file, 'r') as f:
        ips = f.read().split('\n')
    return ips


def print_res(r, *args, **kwargs):
    """Callback function that prints the result"""
    try:
        json = r.json()
        print 'Ip: {ip}, Country: {country}'.format(
            ip=json['ip'], country=json['country'])
    except:
        pass


def get(urls):
    """Reduce number of parameters to the get method"""
    for url in urls:
        yield grequests.get(url, session=s,
                            hooks=dict(response=print_res))


def main():
    """Main method"""
    ips = read_ips()
    urls = [''.join(['http://www.telize.com/geoip/', ip]) for ip in ips]

    grequests.map(get(urls), size=10)


if __name__ == '__main__':
    main()
