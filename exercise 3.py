
import json
import csv, operator

with open('precipitation.json', encoding='utf-8') as file: 
    precipitation = json.load(file)
print(precipitation)

with open('stations.csv', encoding = 'utf-8') as file:
    stations = file.read()
print(stations)

for y in precipitation:
    full_date = y['date']
    year, month, day = map(int, full_date.split('-'))
    y['year'] = year
    y['month'] = month
    y['day'] = day 


month_list = []
months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
for y in months:
    total = 0 
    for input in precipitation: 
        if y == input['month']: 
            total += input['value']
    month_list.append(total)

yearly_total_precipitation = []
yearly_total_seattle = sum(month_list)
yearly_total_precipitation.append(yearly_total_seattle)


relative_list = []
for r in month_list:
    relative = r/yearly_total_seattle
    relative_list.append(relative)
print(relative_list)
