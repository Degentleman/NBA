# Import libraries
import openlocationcode as olc
from haversine import haversine, Unit

# Define functions
def find_coords(team_code, locations):
    """Returns the arena name and coordinates of an NBA team."""
    arena_name = locations[locations["Code"] == team_code]["Arena"].item()
    arena_coords = locations[locations["Code"] == team_code]["Coords"].item()
    return arena_name, arena_coords

def calculate_distance(coords1, coords2):
    """Returns the distance between two coordinates in miles."""
    distance = haversine(coords1, coords2, unit=Unit.MILES)
    return distance

# Read CSV file
locations = pd.read_csv("NBA PBP - Team Legend.csv", delimiter=",")

# Use Google's OpenLocationCode (OLC) to determine latitude and longitude
locations["Coords"] = locations["Plus Code"].apply(lambda x: (olc.decode(x).latitudeCenter, olc.decode(x).longitudeCenter))

# Pass two team codes through the functions to calculate the haversine distance
team1, team2 = "LAL", "ATL"

team1_arena, team1_coords = find_coords(team1, locations)
team2_arena, team2_coords = find_coords(team2, locations)
travel_dist = calculate_distance(team1_coords, team2_coords)

# Print the distance
print(f"The distance between {team1_arena} & {team2_arena} is {round(travel_dist, 2)} miles.")
