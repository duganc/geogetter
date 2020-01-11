import requests
import csv
import argparse

parser = argparse.ArgumentParser(description='Convert a list of addresses to latitudes and longitudes using OpenCage geocoding API.')
parser.add_argument('api_key', type=str,
                    help='API key for OpenCage API')
parser.add_argument('address_path', type=str)
parser.add_argument('output_path', type=str)

def get_lat_long(api_key, address_path, output_path):
	with open(address_path) as csv_file:
    readCSV = csv.reader(csv_file, delimiter=',')
    addresses = []
    for row in readCSV:
        assert len(row) == 1, "Too many records per row: {}".format(row)
        addresses.push(row[0])

    results = _fetch_addresses(token, addresses)
    print(results)



def _fetch_addresses(token, addresses)
	assert type(addresses) == list
	assert all(type(s) for s in addresses)

	return ['895 West End Ave.', '0.0', '0.0']


