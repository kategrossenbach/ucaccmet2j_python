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

month_list = []
months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
for y in months:
    sum = 0 
    for input in precipitation_list: 
        if y == input['month']: 
            sum += input['value']
    month_list.append(sum)

print(month_list)