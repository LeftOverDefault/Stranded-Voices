from src.objects.misc import misc_objects
from src.scenes.game_screens.game_screen import GameScreen
from src.scripts.checks.check_errors import PlaceLocationError

def PlacementHandler(player, object):
    object_dict = misc_objects[object]
    if player.current_location not in object_dict["place_locations"]:
        player.previous_error = PlaceLocationError(player, object)
        GameScreen(player)
        player.Prompt()
    else:
        player.previous_error = f"The \"{object}\" has been placed."