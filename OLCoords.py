#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This script calculates the distance between two NBA teams.
@author: Degentleman
Created on Tue Dec  1 16:40:42 2020
"""
import openlocationcode as olc
import pandas as pd
from haversine import haversine, Unit

def calculate_distance_olc(coords1, coords2):
    """Returns the distance between two coordinates in miles."""
    try:
        distance = haversine(coords1, coords2, unit=Unit.MILES)
    except ValueError:
        raise ValueError("Invalid coordinates")
    return distance

def find_coords(team_code, locations):
    """Returns the arena name and coordinates of an NBA team."""
    arena_name = locations.loc[locations["Code"] == team_code, "Arena"].item()
    arena_coords = locations.loc[locations["Code"] == team_code, "Coords"].item()
    return arena_name, arena_coords

# Read CSV file
locations = pd.read_csv("NBA PBP - Team Legend.csv", delimiter=",")

# Use Google's OpenLocationCode (OLC) to determine latitude and longitude
locations["Coords"] = locations["Plus Code"].apply(lambda x: (olc.decode(x).latitudeCenter, olc.decode(x).longitudeCenter))

# Pass two team codes through the functions to calculate the haversine distance
team1, team2 = "LAL", "ATL"

team1_arena, team1_coords = find_coords(team1, locations)
team2_arena, team2_coords = find_coords(team2, locations)
travel_dist = calculate_distance_olc(team1_coords, team2_coords)

# Print the arena names and distance
print(f"The distance between {team1_arena} & {team2_arena} is {round(travel_dist, 2)} miles.")
