from src.objects.misc import misc_objects
from src.scenes.game_screens.game_screen import GameScreen
from src.utils.errors import NotInLocationError, InventorySpaceError, ObjectNotExistsError
from src.utils.support import *


def TakeHandler(player, object):
	if "-" in object:
		u_object = ConvertDashUnderscore(object)
	else:
		u_object = object
	if u_object not in misc_objects.keys():
		player.previous_error = ObjectNotExistsError(player, object)
	else:
		object_dict = misc_objects[u_object]
		object_name = object_dict["name"]
		if u_object not in player.current_world[player.current_location]["objects"]:
			player.previous_error = NotInLocationError(player, object)
			GameScreen(player)
		else:
			if len(player.inventory) + 1 > player.inventory_size:
				player.previous_error = InventorySpaceError(player)
				GameScreen(player)
			else:
				player.current_world[player.current_location]["objects"].remove(u_object)
				player.inventory.append(u_object)
				player.previous_error = f"You took the \"{object_name}\"."