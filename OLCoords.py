#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This script calculates the distance between two NBA teams.
@author: Degentleman
Created on Tue Dec  1 16:40:42 2020
"""

import pandas as pd
import openlocationcode as olc
from haversine import haversine, Unit

def calculate_distance(team1, team2):
    """Returns the distance between two NBA teams' arenas in miles."""
    try:
        team1_coords = get_arena_coords(team1)
        team2_coords = get_arena_coords(team2)
        distance = calculate_haversine_distance(team1_coords, team2_coords)
    except (ValueError, KeyError):
        raise ValueError("Invalid team code")
    return distance

def get_arena_coords(team_code):
    """Returns the latitude and longitude coordinates of an NBA team's arena."""
    arena_coords = locations.loc[locations["Code"] == team_code, "Coords"].item()
    return arena_coords

def calculate_haversine_distance(coords1, coords2):
    """Returns the distance between two coordinates in miles."""
    try:
        distance = haversine(coords1, coords2, unit=Unit.MILES)
    except ValueError:
        raise ValueError("Invalid coordinates")
    return distance

# Read the NBA teams' arena data from the CSV file.
locations = pd.read_csv("NBA PBP - Team Legend.csv", delimiter=",")

# Use Google's OpenLocationCode (OLC) to determine the latitude and longitude of the arenas.
locations["Coords"] = locations["Plus Code"].apply(lambda x: (olc.decode(x).latitudeCenter, olc.decode(x).longitudeCenter))

# Pass two team codes through the function to calculate the haversine distance.
team1, team2 = "LAL", "ATL"
distance = calculate_distance(team1, team2)

# Print the arena names and distance.
print(f"The distance between {team1} & {team2} is {round(distance, 2)} miles.")
