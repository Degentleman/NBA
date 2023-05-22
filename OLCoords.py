#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This script calculates the distance between two NBA teams.
@author: Degentleman
Created on Tue Dec  1 16:40:42 2020
"""
import pandas as pd
import matplotlib.pyplot as plt
from haversine import haversine, Unit


def calculate_distance(team1, team2, distance_unit=Unit.MILES):
    """Returns the distance between two NBA teams in the specified unit."""
    try:
        team1_coords = get_arena_coords(team1)
        team2_coords = get_arena_coords(team2)
        distance = haversine(team1_coords, team2_coords, unit=distance_unit)
    except ValueError:
        raise ValueError("Invalid team code")
    return distance


def get_arena_coords(team_code):
    """Returns the latitude and longitude coordinates of an NBA team's arena."""
    arena_coords = locations.loc[locations["Code"] == team_code, "Coords"].item()
    return arena_coords


def plot_basketball_court(team_code):
    """Plots the basketball court with the specified team's code at the center."""
    plt.figure()
    plt.plot([0, 94], [0, 50], color="black")
    plt.plot([0, 94], [0, 42], color="gray")
    plt.plot([0, 28], [0, 42], color="gray")
    plt.plot([0, 28], [0, 0], color="gray")
    plt.plot([28, 94], [0, 0], color="gray")
    plt.plot([28, 94], [42, 0], color="gray")
    plt.plot([0, 94], [42, 0], color="gray")
    plt.plot([0, 94], [50, 0], color="black")
    plt.text(47, 25, team_code, fontsize=14, ha="center", va="center")
    plt.title("Basketball Court")
    plt.xlabel("X-Coordinate")
    plt.ylabel("Y-Coordinate")
    plt.savefig("basketball_court.png")
    plt.show()


# Read the CSV file into a Pandas DataFrame.
df = pd.read_csv("players.csv")

# Read the CSV file with team locations.
locations = pd.read_csv("NBA PBP - Team Legend.csv", delimiter=",")

# Get the team codes for the Los Angeles Lakers and the Atlanta Hawks.
team1_code = "LAL"
team2_code = "ATL"

# Calculate the distance between the two teams.
distance = calculate_distance(team1_code, team2_code, Unit.MILES)

# Plot the basketball court with the home team's code.
plot_basketball_court(team1_code)

# Print the distance between the two teams.
print(f"The distance between {team1_code} and {team2_code} is {round(distance, 2)} miles.")

# Get the away team code and their distance traveled to the home team's court.
away_team_code = "ATL"
away_team_distance = calculate_distance(team2_code, team1_code, Unit.MILES)

# Plot the away team code and their distance traveled on the basketball court plot.
plt.plot([away_team_distance], [away_team_code], marker="o", color="red")

# Show the court plot.
plt.show()
