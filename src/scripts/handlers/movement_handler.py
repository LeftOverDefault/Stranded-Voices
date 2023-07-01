from src.utils.support import *

def Move(player, direction):
	if direction != None or direction != "":
		if direction.lower() not in ["north", "north-east", "north-west", "east", "south", "south-east", "south-west", "west", "up", "down"]:
			return "direction_error"
		if direction in ["north-east", "north-west", "south-east", "south-west"]:
			direction = ConvertDashUnderscore(direction)
		if player.current_world[player.current_location]["directions"][direction] == None:
			return "location_error"
		player.current_location = player.current_world[player.current_location]["directions"][direction]