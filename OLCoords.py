#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This script calculates the distance between two NBA teams.
@author: Degentleman
Created on Tue Dec  1 16:40:42 2020
"""
import openlocationcode as olc
from haversine import haversine, Unit
import pandas as pd

def calculate_distance_between_teams(team1, team2):
    """Calculates the distance between two NBA teams.

    Args:
        team1 (str): The code of the home team.
        team2 (str): The code of the away team.

    Returns:
        float: The distance between the two teams in miles.
    """
    # Get the coordinates of the two teams.
    home_coords = locations[locations['Code'] == team1]['Coords'].values[0]
    away_coords = locations[locations['Code'] == team2]['Coords'].values[0]

    # Calculate the distance between the two teams.
    distance = haversine(home_coords, away_coords, unit=Unit.MILES)

    return distance

# Read the NBA PBP - Team Legend.csv file.
locations = pd.read_csv('NBA PBP - Team Legend.csv', delimiter=",")

# Use Google's OpenLocationCode (OLC) to determine Latitude and Longitude.
locations['Coords'] = locations['Plus Code'].apply(lambda x: (olc.decode(x).latitudeCenter, olc.decode(x).longitudeCenter))

# Prompt the user to input the home and away team's code.
home_team_code = input("Enter the home team's code: ")
away_team_code = input("Enter the away team's code: ")

# Calculate the distance between the two teams.
distance = calculate_distance_between_teams(home_team_code, away_team_code)

# Print the distance to the console.
print(f"The distance between the two teams ({away_team_code} @ {home_team_code}) is {round(distance, 2)} miles.")
