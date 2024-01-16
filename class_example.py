import json

with open('precipitation.json') as file:
    measurements = json.load(file)

total_precipitation = 0
for measurement in measurements: 
    if measurement['station'] == "GHCND:US1WAKG0038":
        total_precipitation = total_precipitation + measurement['value']

print(total_precipitation)