import json
import csv

with open('precipitation.json') as file:
    measurements = json.load(file)

with open('stations.csv') as file:
    reader = csv.DictReader(file)
    stations = list(reader)

for station in stations:
    total_precipitation = 0
    monthly_precipitation = [0] * 12 
    for measurement in measurements: 
        if measurement['station'] == station['Station']:
            date = measurement['date'].split('-')
            month = int(date[1])
            total_precipitation = total_precipitation + measurement['value']
            monthly_precipitation[month - 1] = monthly_precipitation[month - 1]\
                + measurement['value']
    print(monthly_precipitation)
    print(total_precipitation)

    relative_precipitation = []
    for precipitation in monthly_precipitation:
        relative_precipitation.append(precipitation/total_precipitation)

    result = {
        station['Location']: {
        "station": station['Station'],
        "state": station['State'],
        "total_monthly_precipitation": monthly_precipitation,
        "total_yearly_precipitation": total_precipitation,
        "relative_monthly_precipitation": relative_precipitation
        }
    },

print(result)

