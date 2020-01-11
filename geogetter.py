import requests
import csv
import argparse

parser = argparse.ArgumentParser(description='Convert a list of addresses to latitudes and longitudes using OpenCage geocoding API.')
parser.add_argument('api_key', type=str, help='API key for OpenCage API')
parser.add_argument('address_path', type=str)
parser.add_argument('output_path', type=str)

def get_lat_long(api_key, address_path, output_path):
	assert type(api_key) == str
	assert type(address_path) == str
	assert type(output_path) == str
	with open(address_path) as csv_file:
		readCSV = csv.reader(csv_file, delimiter=',')
		addresses = []
		for row in readCSV:
			assert len(row) == 4, "Too many records per row: {}".format(row)
			address = ', '.join(row)
			addresses.append(address)

		results = _fetch_addresses(api_key, addresses)
		print('Got results: {}'.format(results))
		with open(output_path, "a", newline='') as f:
			writer = csv.writer(f)
			for row in results:
				print('Writing row: {}'.format(row))
				writer.writerow(row)


def _fetch_addresses(api_key, addresses):
	assert type(addresses) == list
	assert all(type(s) for s in addresses)

	results = []
	for address in addresses:
		bounds = ','.join((str(n) for n in [-74.024001, 40.700865, -73.907341, 40.879212]))
		endpoint = 'https://api.opencagedata.com/geocode/v1/json?q={}&key={}&bounds={}'.format(address, api_key, bounds);
		response = requests.get(endpoint)
		assert response.status_code == 200, 'Invalid response: {}\n{}'.format(response.status_code, response.text)
		json = response.json()
		assert 'results' in json.keys(), 'API returned no results: {}\n{}'.format(response.status_code, response.text)
		response_results = json['results'][0]
		row = [address, response_results['formatted'], response_results['geometry']['lat'], response_results['geometry']['lng']]
		print('Got row: {}'.format(row))
		results.append(row)

	return results



args = parser.parse_args()
get_lat_long(args.api_key, args.address_path, args.output_path)
