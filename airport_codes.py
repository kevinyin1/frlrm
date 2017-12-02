"""
Learning to use Google Geocode API for project at YHack
"""

import requests
import json

codes = ["JFK", "ABQ"]
apikey = "AIzaSyC_phvxZIy7dHAEh_lu7T2p0ZnHhZBDZsw"
results = []
result_str = ""

for code in codes:
	info = requests.post('https://maps.googleapis.com/maps/api/geocode/json?address=' + code + 'AIRPORT&key=' + apikey)
	info = info.json()
	print(info)
	lat = info['results'][0]['geometry']['location']
	print(lat)
	results.append(lat)
	results.append(", ")

del results[-1]

for result in results:
	result_str = result_str + str(result)

result_str = str.replace(result_str, '\'', '')

print(result_str)
with open ('result.txt', "a") as text_file:
	text_file.write(result_str)