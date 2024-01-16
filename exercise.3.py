#What I want to do is have python read the csv file. 
#I then want to create the loop where it goes through and seperates the values by location
#Finally I want to run the calculations on each. I will attempt to do this in the loop above. 
#my goal is for python to identify the different codes, and run through the operations in a for-loop for each station code.

import json

with open('precipitation.json', encoding='utf-8') as file: 
    precipitation = json.load(file)

import csv
from csv import DictReader
#I 
with open('stations.csv', encoding = 'utf-8') as file:
    stations= DictReader(file)
    items = list(stations)


#create a list including only Seattle 

#what I want to do is ascociate all codes for a city with one seperate list within a new dictionary 
    #I was trying to sort stations but this didn't work.
station_sort = []
for station in items:
    if station 

#if I had had more time, I would have hopefully found a way to seperate the stations, or to have python identify the seperate station codes and run through my previously written code for each station. 
#I ran out of time, sorry it's so incomplete!