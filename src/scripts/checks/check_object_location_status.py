from src.objects.misc import misc_objects


def CheckObjectStatus(player):
    index = 0
    for object in misc_objects:
        if misc_objects[object]["special_object"] != True:
            pass
        else:
            if list(misc_objects.keys())[index] in player.current_world[player.current_location]["placed_objects"]:
                if player.current_location == misc_objects[object]["correct_location"]:
                    if object == "fuse":
                        player.comms = True
                    
                else:
                    pass
            else:
                pass
        
        index += 1