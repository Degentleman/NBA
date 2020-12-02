#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 16:40:42 2020

@author: Degentleman
"""
import openlocationcode as olc
import pandas as pd
import haversine as hs
from haversine import Unit

# Search function returns NBA team's arena name and the coordinates tuple.
def find_coords(team_code, locations):
    arena_name = locations[(locations.Code == team_code)].Arena.item()
    arena_coords = locations[(locations.Code == team_code)].Coords.item()
    return(arena_name, arena_coords)

# Function calculates distance (in miles) between two coordinate tuples.
def calc_dist(arena1, arena2):
    dist = hs.haversine(arena1, arena2, unit=Unit.MILES)    
    return(dist)

# CSV of NBA arenas and their corresponding Google Plus Codes.
locations = pd.read_csv('NBA PBP - Team Legend.csv', delimiter=",")

# Use Google's OpenLocationCode (OLC) to determine Latitude and Longitude.
locations['Coords'] = locations['Plus Code'].apply(lambda x: (olc.decode(x).latitudeCenter, olc.decode(x).longitudeCenter))

# Pass two team codes through the functions to calculate the haversine distance.
team1, team2 = 'LAL', 'ATL'

arena1, arena1_coords = find_coords(team1, locations)
arena2, arena2_coords = find_coords(team2, locations)
travel_dist = calc_dist(arena1_coords, arena2_coords)

print('The distance between '+arena1+' & '+arena2+' is '+str(round(travel_dist,2))+' miles.')
