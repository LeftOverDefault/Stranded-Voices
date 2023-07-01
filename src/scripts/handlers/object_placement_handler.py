from src.objects.misc import misc_objects
from src.scenes.game_screens.game_screen import GameScreen
from src.scripts.checks.check_errors import PlaceObjectError, PlaceLocationError, NotInInventoryError, InventorySpaceError
from src.utils.support import *


def PlacementHandler(player, object):
    if "-" in object:
        u_object = ConvertDashUnderscore(object)
        object_dict = misc_objects[u_object]
        object_name = object_dict["name"]
    else:
        player.previous_error = PlaceObjectError(player, object)
        GameScreen(player)
        player.Prompt()
    if player.current_location not in object_dict["place_locations"]:
        player.previous_error = PlaceLocationError(player, object_name)
        GameScreen(player)
        player.Prompt()
    else:
        if u_object not in player.inventory:
            player.previous_error = NotInInventoryError(player, object)
            GameScreen(player)
            player.Prompt()
        else:
            if len(player.inventory) + 1 > player.inventory_size:
                player.previous_error = InventorySpaceError(player)
                GameScreen(player)
                player.Prompt()
            else:
                player.inventory.pop(u_object)
                player.current_world[player.current_location]["placed_objects"].append(u_object)
                player.previous_error = f"The \"{object_name}\" has been placed."