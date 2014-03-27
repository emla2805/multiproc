import requests
from multiprocessing.dummy import Pool as ThreadPool


def read_ips(file='./ips.txt'):
    """Read ips from file and return a list"""
    with open(file, 'r') as f:
        ips = f.readlines()
    return ips


def main():
    """Main method"""

    # ips = ['80.216.16.246', '74.118.91.238', '197.136.43.2']
    ips = read_ips()

    urls = [''.join(['http://www.telize.com/geoip/', ip]) for ip in ips]

    # Make the pool of workers
    pool = ThreadPool(10)

    results = pool.map(requests.get, urls)

    for r in results:
        json = r.json()
        print 'Ip: {ip}, Country: {country}'.format(
            ip=json['ip'], country=json['country'])

if __name__ == '__main__':
    main()
