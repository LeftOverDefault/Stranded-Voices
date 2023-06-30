from src.scripts.handlers.event_handler import RunEvent

def CheckPuzzles(player):
    world = player.current_world
    location = player.current_location
    require, required_object = world[location]["puzzle_answer"].split(":")
    if require == "requires_item":
        if required_object in player.inventory:
            world[location]["solved"] = True
            if world[location]["event"] == None:
                print("Nothing happens")
            else:
                RunEvent(player, world[location]["event"])


def UpdatePuzzles(player):
    pass
