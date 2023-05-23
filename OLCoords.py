#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This script calculates the distance between two NBA teams.
@author: Degentleman
Created on Tue Dec  1 16:40:42 2020
"""

import openlocationcode as olc
import pandas as pd

# CSV of NBA arenas and their corresponding Google Plus Codes.
locations = pd.read_csv('NBA PBP - Team Legend.csv', delimiter=",")

# Use Google's OpenLocationCode (OLC) to determine Latitude and Longitude.
locations['Coords'] = locations['Plus Code'].apply(lambda x: (olc.decode(x).latitudeCenter, olc.decode(x).longitudeCenter))

# Print the latitude and longitude coordinates of the first row in the DataFrame.
print(locations.iloc[0]['Coords'])
