#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This script calculates the distance between two NBA teams.
@author: Degentleman
Created on Tue Dec  1 16:40:42 2020
"""
import openlocationcode as olc
from geopy.distance import geodesic
import pandas as pd

# Read the NBA PBP - Team Legend.csv file.
locations = pd.read_csv('NBA PBP - Team Legend.csv', delimiter=",")

# Use Google's OpenLocationCode (OLC) to determine Latitude and Longitude.
locations['Coords'] = locations['Plus Code'].apply(lambda x: (olc.decode(x).latitudeCenter, olc.decode(x).longitudeCenter))

# Define the function to calculate the distance between two teams.
def calculate_distance_between_teams(team1, team2):
  """Calculates the distance between two NBA teams.

  Args:
    team1: The code of the home team.
    team2: The code of the away team.

  Returns:
    The distance between the two teams in miles.
  """

  # Get the coordinates of the two teams.
  home_coords = locations[locations['Code'] == team1]['Coords'].values[0]
  away_coords = locations[locations['Code'] == team2]['Coords'].values[0]

  # Calculate the distance between the two teams.
  distance = geodesic(home_coords, away_coords).miles

  return distance

# Prompt the user to input the home and away team's code.
print("Enter the home team's code: ")
home_team_code = input()
print("Enter the away team's code: ")
away_team_code = input()

# Calculate the distance between the two teams.
distance = calculate_distance_between_teams(home_team_code, away_team_code)

# Round the distance to two decimal places.
distance = round(distance, 2)

# Print the distance to the console.
print("The distance between the two teams is {} miles.".format(distance))
