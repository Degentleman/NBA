#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This script calculates the distance between two NBA teams.
@author: Degentleman
Created on Tue Dec  1 16:40:42 2020
"""

import plus as olc
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

# Get the team codes from the user.
home_team_code = input("Enter the code for the home team: ")
away_team_code = input("Enter the code for the away team: ")

# Find the arena names and coordinates for the two teams.
home_team_arena, home_team_coords = find_coords(home_team_code, locations)
away_team_arena, away_team_coords = find_coords(away_team_code, locations)

# Calculate the distance between the two teams.
travel_dist = calc_dist(home_team_coords, away_team_coords)

# Print the distance between the two teams.
print('The distance between '+home_team_arena+' & '+away_team_arena+' is '+str(round(travel_dist,2))+' miles.')
