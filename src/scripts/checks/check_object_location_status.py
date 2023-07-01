from src.objects.misc import misc_objects


def CheckObjectStatus(player):
    index = 0
    for i in misc_objects:
        if misc_objects[i]["special_object"] != True:
            pass
        else:
            if list(misc_objects.keys())[index] in player.current_world[player.current_location]["placed_objects"]:
                if player.current_location == misc_objects[i]["correct_location"]:
                    if i == "fuse_1":
                        player.comms = True
                else:
                    pass
            else:
                pass
        
        index += 1