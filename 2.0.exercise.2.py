import json

with open('precipitation.json', encoding='utf-8') as file: 
    precipitation = json.load(file)
print(precipitation)

#create a list including only Seattle 
precipitation_list = []
for x in precipitation:
    if "GHCND:US1WAKG0038" == x['station']:
        precipitation_list.append(x)

#split the date into year, day and month to calculate monthly value 
for y in precipitation_list:
    full_date = y['date']
    year, month, day = map(int, full_date.split('-'))
    y['year'] = year
    y['month'] = month
    y['day'] = day 
print(precipitation_list)

#calculate monthly totals 
monthly_precipitation = []
months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
for y in months:
    total = 0 
    for input in precipitation_list: 
        if y == input['month']: 
            total += input['value']
    monthly_precipitation.append(total)

print(monthly_precipitation)

#calculate yearly totals
yearly_total_precipitation = []
yearly_total_seattle = sum(month_list)
yearly_total_precipitation.append(yearly_total_seattle)

print(yearly_total_precipitation)

#calculate relative monthly totals, using yearly total from abovee
relative_list = []
for r in month_list:
    relative = r/yearly_total_seattle
    relative_list.append(relative)
print(relative_list)

#update results file
with open('results.json', 'w', encoding = 'utf-8') as file: 
    json.dump(relative_list, file, indent = 4)