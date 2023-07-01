from src.objects.misc import misc_objects
from src.scenes.game_screens.game_screen import GameScreen
from src.utils.errors import PlaceObjectError, NotInInventoryError, LocationSpaceError
from src.utils.support import *
from src.utils.constants import *


def PlacementHandler(player, object):
	if "-" in object:
		u_object = ConvertDashUnderscore(object)
		object_dict = misc_objects[u_object]
		object_name = object_dict["name"]
		if u_object not in player.inventory:
			player.previous_error = NotInInventoryError(player, object)
			GameScreen(player)
		else:
			if len(player.current_world[player.current_location]["placed_objects"]) + 1 > LOCATION_PLACEMENT_SIZE:
				player.previous_error = LocationSpaceError(player)
				GameScreen(player)
			else:
				player.inventory.remove(u_object)
				player.current_world[player.current_location]["placed_objects"].append(u_object)
				player.previous_error = f"The \"{object_name}\" has been placed."
	else:
		player.previous_error = PlaceObjectError(player, object)
		GameScreen(player)