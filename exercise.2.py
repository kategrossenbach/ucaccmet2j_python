import json

with open('precipitation.json', encoding='utf-8') as file: 
    precipitation = json.load(file)
print(precipitation)

precipitation_list = []
for x in precipitation:
    if "GHCND:US1WAKG0038" == x['station']:
        precipitation_list.append(x)

for y in precipitation_list:
    full_date = y['date']
    year, month, day = map(int, full_date.split('-'))
    y['year'] = year
    y['month'] = month
    y['day'] = day 
print(precipitation_list)

year = [2010]
total_yearly = []
for y in year: 
    sum = 0 
    for input in precipitation_list:
        if y == input['year']:
            sum += input['value']
    total_yearly.append(sum)
print(total_yearly)