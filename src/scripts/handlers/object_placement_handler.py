from src.objects.misc import misc_objects
from src.scenes.game_screens.game_screen import GameScreen
from src.utils.constants import *
from src.utils.errors import LocationSpaceError, NotInInventoryError, ObjectNotExistsError
from src.utils.support import *


def PlacementHandler(player, object):
	if "-" in object:
		u_object = ConvertDashUnderscore(object)
	else:
		u_object = object
	if u_object not in misc_objects.keys():
		player.previous_error = ObjectNotExistsError(player, object)
	else:
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