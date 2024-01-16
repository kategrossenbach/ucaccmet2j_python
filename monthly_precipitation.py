import json

with open('precipitation.json', encoding='utf-8') as file: 
    precipitation = json.load(file)
print(precipitation)


for dictionary in range(len(precipitation)):
    print(precipitation[dictionary])

precipitation_list = []
for x in precipitation:
    if "GHCND:US1WAKG0038" == x['station']:
        precipitation_list.append(x)
print (precipitation_list)