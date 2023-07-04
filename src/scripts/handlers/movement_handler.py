from src.scenes.game_screens.game_screen import GameScreen
from src.scenes.transition_screens.movement_screen import MovementScreen
from src.utils.support import *
from src.utils.errors import DirectionError, LocationError

def MovementHandler(player, direction):
	if direction.lower() not in ["north", "north-east", "north-west", "east", "south", "south-east", "south-west", "west", "up", "down"]:
		player.previous_error = DirectionError(player, direction)
		GameScreen(player)
	if direction in ["north-east", "north-west", "south-east", "south-west"]:
		direction = ConvertDashUnderscore(direction)
	if player.current_world[player.current_location]["directions"][direction] == None:
		player.previous_error = LocationError(player, direction)
		GameScreen(player)
	old_location = player.current_world[player.current_location]["name"]
	player.current_location = player.current_world[player.current_location]["directions"][direction]
	MovementScreen(player, direction, old_location)
	GameScreen(player)
