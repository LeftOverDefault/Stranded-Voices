import os

from src.entities.entities import entities
from src.objects.misc import misc_objects
from src.utils.colors import *


def GameScreen(player):
	location_name = player.current_world[player.current_location]["name"]
	location_examination = player.current_world[player.current_location]["examination"]

	room_description_line_1, room_description_line_2, room_description_line_3, room_description_line_4 = player.current_world[player.current_location]["description"].split("\l")
	
	object_descriptions = ["", "", ""]
	for i in range(len(player.current_world[player.current_location]["objects"])):
		object_descriptions[i] = misc_objects[player.current_world[player.current_location]["objects"][i]]["description"]
	
	entity_descriptions = ["", ""]
	for i in range(len(player.current_world[player.current_location]["entities"])):
		entity_descriptions[i] = entities[player.current_world[player.current_location]["entities"][i]]["description"]

	direction_names = {
		"north": "None",
		"east": "None",
		"south": "None",
		"west": "None",
		"north_east": "None",
		"north_west": "None",
		"south_east": "None",
		"south_west": "None",
		"up": "None",
		"down": "None"
	}

	for direction in player.current_world[player.current_location]["directions"]:
		if player.current_world[player.current_location]["directions"][direction] == None:
			direction_names[direction] = "None"
		else:
			direction_names[direction] = player.current_world[player.current_world[player.current_location]["directions"][direction]]["name"]

	if location_examination == None:
		examination_line_1, examination_line_2 = "None", "None"
	else:
		examination_line_1, examination_line_2 = location_examination.split("\l")

	parts_descriptions = ["", "", ""]
	for i in range(len(player.current_world[player.current_location]["placed_objects"])):
		parts_descriptions[i] = misc_objects[player.current_world[player.current_location]["placed_objects"][i]]["description"]
	
	inventory = ["", "", "", "", "", "", "", "", "", "", "", "", ""]
	for i in range(len(player.inventory)):
		inventory[i] = misc_objects[player.inventory[i]]["name"]

	os.system("clear")
	print(len("                                    "))
	print(f"        ┏━━━━━━━━━━━━━━┓        ┏━━━━━━━━━━━━━━┓        ┏━━━━━━━━━━━━━━┓        ┏━━━━━━━━━━━━━━┓")
	print(f"┏━━━━━━━┫  {CYAN}[ PUREYA ]{WHITE}  ┣━━━━━━━━┫ {GREEN}[HP] {player.hp}/100{WHITE} ┣━━━━━━━━┫ {RED}[ COMMS ] --{WHITE} ┣━━━━━━━━┫ {BLUE}[ SETTINGS ]{WHITE} ┣━━━[ {YELLOW}TASUKU{WHITE} ]━━━┓")
	print(f"┃       ┗━━━━━━━━━━━━━━┛        ┗━━━━━━━━━━━━━━┛        ┗━━━━━━━━━━━━━━┛        ┗━━━━━━━━━━━━━━┫                ┃")
	print(f"┃ {YELLOW}┏" + (f"━" * (len(location_name) + 2)) + f"┓{WHITE}" + (f" " * (71 - (len(location_name) + 2))) + f"                    ┃                ┃")
	print(f"┃ {YELLOW}┃ {location_name} ┃{WHITE}" + (f" " * (71 - (len(location_name) + 2))) + f"                    ┃                ┃")
	print(f"┃ {YELLOW}┣" + (f"━" * (len(location_name) + 2)) + f"┛{WHITE}" + (f" " * (71 - (len(location_name) + 2))) + f"                    ┃                ┃")
	print(f"┃ {YELLOW}┣╸{WHITE}{room_description_line_1}" + (f" " * (94 - (len(room_description_line_1) + 3))) + f"┃                ┃")
	print(f"┃ {YELLOW}┣╸{WHITE}{room_description_line_2}" + (f" " * (94 - (len(room_description_line_2) + 3))) + f"┃                ┃")
	print(f"┃ {YELLOW}┣╸{WHITE}{room_description_line_3}" + (f" " * (94 - (len(room_description_line_3) + 3))) + f"┃                ┃")
	print(f"┃ {YELLOW}┗╸{WHITE}{room_description_line_4}" + (f" " * (94 - (len(room_description_line_4) + 3))) + f"┃                ┃")
	print(f"┃   🮥  " + object_descriptions[0] + (f" " * (74 - (len(object_descriptions[0]) + 6))) + f"                    ┃                ┃")
	print(f"┃   🮥  " + object_descriptions[1] + (f" " * (74 - (len(object_descriptions[1]) + 6))) + f"                    ┃                ┃")
	print(f"┃   🮥  " + object_descriptions[2] + (f" " * (74 - (len(object_descriptions[2]) + 6))) + f"                    ┃                ┃")
	print(f"┃   🮥  " + entity_descriptions[0] + (f" " * (74 - (len(entity_descriptions[0]) + 6))) + f"                    ┃                ┃")
	print(f"┃   🮥  " + entity_descriptions[1] + (f" " * (74 - (len(entity_descriptions[1]) + 6))) + f"┏━━━━━[ {YELLOW}YOROI{WHITE} ]━━━━━┻━━━━━━━━━━━━━━━━┫")
	print(f"┃                                                                          ┃                                    ┃")
	print(f"┃ {MAGENTA}NORTH |{WHITE} " + direction_names["north"] + (f" " * (29 - len(direction_names["north"]))) + f"{MAGENTA}EAST |{WHITE} " + direction_names["east"] + (f" " * (29 - len(direction_names["east"]))) + f"┃ {BLUE}┏╸{WHITE}{inventory[0]}" + (" " * (36 - (len(inventory[0]) + 3))) + "┃")
	print(f"┃ {MAGENTA}SOUTH |{WHITE} " + direction_names["south"] + (f" " * (29 - len(direction_names["south"]))) + f"{MAGENTA}WEST |{WHITE} " + direction_names["west"] + (f" " * (29 - len(direction_names["west"]))) + f"┃ {BLUE}┣╸{WHITE}{inventory[1]}" + (" " * (36 - (len(inventory[1]) + 3))) + "┃")
	print(f"┃ {MAGENTA}NORTH-EAST |{WHITE} " + direction_names["north_east"] + (f" " * (24 - len(direction_names["north_east"]))) + f"{MAGENTA}NORTH-WEST |{WHITE} " + direction_names["north_west"] + (f" " * (23 - len(direction_names["north_west"]))) + f"┃ {BLUE}┣╸{WHITE}{inventory[2]}" + (" " * (36 - (len(inventory[2]) + 3))) + "┃")
	print(f"┃ {MAGENTA}SOUTH-EAST |{WHITE} " + direction_names["south_east"] + (f" " * (24 - len(direction_names["south_east"]))) + f"{MAGENTA}SOUTH-WEST |{WHITE} " + direction_names["south_west"] + (f" " * (23 - len(direction_names["south_west"]))) + f"┃ {BLUE}┣╸{WHITE}{inventory[3]}" + (" " * (36 - (len(inventory[3]) + 3))) + "┃")
	print(f"┃ {MAGENTA}UP |{WHITE} " + direction_names["up"] + (f" " * (32 - len(direction_names["up"]))) + f"{MAGENTA}DOWN |{WHITE} " + direction_names["down"] + (f" " * (29 - len(direction_names["down"]))) + f"┃ {BLUE}┣╸{WHITE}{inventory[4]}" + (" " * (36 - (len(inventory[4]) + 3))) + "┃")
	print(f"┃                                                                          ┃ {BLUE}┣╸{WHITE}{inventory[5]}" + (" " * (36 - (len(inventory[5]) + 3))) + "┃")
	print(f"┣━[ {YELLOW}ROGU{WHITE} ]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫ {BLUE}┣╸{WHITE}{inventory[6]}" + (" " * (36 - (len(inventory[6]) + 3))) + "┃")
	print(f"┃                                                                          ┃ {BLUE}┣╸{WHITE}{inventory[7]}" + (" " * (36 - (len(inventory[7]) + 3))) + "┃")
	print(f"┃ {BLUE}┏╸{WHITE}{examination_line_1}" + (f" " * (71 - (len(examination_line_1)))) + f"┃ {BLUE}┣╸{WHITE}{inventory[8]}" + (" " * (36 - (len(inventory[8]) + 3))) + "┃")
	print(f"┃ {BLUE}┣╸{WHITE}{examination_line_2}" + (f" " * (71 - (len(examination_line_2)))) + f"┃ {BLUE}┣╸{WHITE}{inventory[9]}" + (" " * (36 - (len(inventory[9]) + 3))) + "┃")
	print(f"┃ {BLUE}┗╸{WHITE}{examination_line_1}" + (f" " * (71 - (len(examination_line_1)))) + f"┃ {BLUE}┣╸{WHITE}{inventory[10]}" + (" " * (36 - (len(inventory[10]) + 3))) + "┃")
	print(f"┃ {GREEN}# {player.previous_input}{WHITE}", (f" " * (69 - len(player.previous_input))), f"┃ {BLUE}┣╸{WHITE}{inventory[11]}" + (" " * (36 - (len(inventory[11]) + 3))) + "┃")
	print(f"┃ {RED}# {player.previous_error}{WHITE}", (f" " * (69 - len(player.previous_error))), f"┃ {BLUE}┗╸{WHITE}{inventory[12]}" + (" " * (36 - (len(inventory[12]) + 3))) + "┃")
	print(f"┃                                                                          ┃                                    ┃")
	print(f"┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
	player.previous_error = ""
	player.Prompt()