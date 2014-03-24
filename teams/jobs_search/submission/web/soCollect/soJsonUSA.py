######################
#Author: Ummata
######################
#This program create json from csv file, only USA jobs considered
#input: filename.csv
#output: filename.json
##### How to run #####
#>python soJsonUSA.py csv_file_name
# 
#Example
#>python soJsonUSA.py 'big data.csv'
#######################
# JSON sturcture
# {City, State, ll, numberOfJobs}
# *ll = (latitude, longtitude)
#######################


import csv
import json
import sys

from geopy import geocoders
from itertools import groupby
from collections import defaultdict
from pprint import pprint

def location(s):
    return s[s.find('(')+1:s.find(')')]

def real_location(s):
    '''Locations are parenthesis, but sometimes there are more than one.
    This function return only locations no drama.
    '''
    # Two parenthesis in a line
    if(s[s.find(')')+1:].find('(') > -1):
        s2 = s[s.find(')')+1:]
        location_array = (location(s), location(s2))
        if location_array[1] == 'allows remote':
            return location_array[0]
        else:
            return location_array[1]
    # only one parenthesis
    else:
        return location(s)

def frequency(mylist):
    D = defaultdict(list)
    for i,item in enumerate(mylist):
        D[item].append(i)
    return {k:len(v) for k,v in D.items() if len(v)>=1}

def dict_location_jobs_from_csv(csv_file):
    ''' key = location, value = number of jobs at this location '''
    locations = [] # a list of locations
    #location_number_of_jobs = {} # 
    with open(csv_file,'rb') as fin:
        reader = csv.reader(fin, delimiter=';', quoting=csv.QUOTE_ALL)
        for line in reader:
            locations.append(real_location(line[0]))
        fin.close()
    return frequency(locations)

def get_city_state_latlong(location):
    # g = geocoders.GeoNames(username='uthangv')
    g = geocoders.GoogleV3() # Google geolocation lib
    if(g.geocode(location) is None):
        return None
    else:
        p, (lat, lng) = g.geocode(location)
        ll = (lat, lng)
        place = p.split(',')
        if len(place) == 3 and place[2].strip() == 'USA':
            p = place.split(',')
            city, state = p[0].strip(), p[1].strip()
            return (city, state, ll)
        else:
            return None

def get_json(location, location_number_of_jobs):
    g = geocoders.GoogleV3() # Google geolocation lib

    # g = geocoders.GeoNames(username='uthangv')
    geo = g.geocode(location)
    if(geo is None):
        return None
    else:
        # print location
        place, (lat, lng) = geo
        if place.find('USA'):
            p = place.split(',')
            city, state = p[0].strip(), p[1].strip()
            ll = (lat, lng)
            json_obj = {
                # 'Place': place,
                'City': city,
                'State': state,
                'll': [ll[1], ll[0]],
                'numberOfJobs': location_number_of_jobs[location]
            }
            return json_obj
        else:
            return None

# #json format
# [{
#   "City":"Los Angeles",
#   "State":"California"
#   "ll":[0.344, 34.3333],
#   "numberOfJobs": 50
# }]
def create_json(location_number_of_jobs):
    output = [] # a list of json objects
    
    # loop to create a list of json objects
    for location in location_number_of_jobs:
        json_obj = get_json(location, location_number_of_jobs)
        if(json_obj is None):
            pass
        else:
            output.append(json_obj)
    return output

def write_json(file_name, json_list):
    with open(file_name, 'w') as outfile:
        json.dump(json_list, outfile)
        outfile.close()

#========= Run scripts here! =========#
if __name__ == '__main__':
    cmdargs = sys.argv
    csv_filename = cmdargs[1]
    json_filename = csv_filename.split('.')[0] + '.json'
    
    location_number_of_jobs = dict_location_jobs_from_csv(csv_filename)
    json_list = create_json(location_number_of_jobs)
    write_json(json_filename,json_list)
