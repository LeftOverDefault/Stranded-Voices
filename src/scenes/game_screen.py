import os

from src.entities.entities import entities
from src.objects.misc import misc_objects
from src.utils.colors import *


def GameScreen(player):
	hp = player.hp
	current_world = player.current_world
	current_location = player.current_location
	location_name = str(current_world[current_location]["name"])
	location_description = current_world[current_location]["description"]
	location_examination = current_world[current_location]["examination"]
	location_directions = current_world[current_location]["directions"]
	location_objects = current_world[current_location]["objects"]
	location_entities = current_world[current_location]["entities"]

	# TODO: Make this shit more efficient.
	try:
		north_location = current_world[location_directions["north"]]
	except:
		north_location = {"name": "None"}
	try:
		east_location = current_world[location_directions["east"]]
	except:
		east_location = {"name": "None"}
	try:
		south_location = current_world[location_directions["south"]]
	except:
		south_location = {"name": "None"}
	try:
		west_location = current_world[location_directions["west"]]
	except:
		west_location = {"name": "None"}
	try:
		north_east_location = current_world[location_directions["north_east"]]
	except:
		north_east_location = {"name": "None"}
	try:
		north_west_location = current_world[location_directions["north_west"]]
	except:
		north_west_location = {"name": "None"}
	try:
		south_east_location = current_world[location_directions["south_east"]]
	except:
		south_east_location = {"name": "None"}
	try:
		south_west_location = current_world[location_directions["south_west"]]
	except:
		south_west_location = {"name": "None"}
	try:
		up_location = current_world[location_directions["up"]]
	except:
		up_location = {"name": "None"}
	try:
		down_location = current_world[location_directions["down"]]
	except:
		down_location = {"name": "None"}

	if location_description == None:
		line_1, line_2, line_3, line_4 = "None", "None", "None", "None"
	else:
		line_1, line_2, line_3, line_4 = location_description.split("\l")

	if location_examination == None:
		examination_line_1, examination_line_2 = "None", "None"
	else:
		examination_line_1, examination_line_2 = location_examination.split("\l")

	if len(location_objects) == 0:
		location_object_1, location_object_2 = {"name": None, "description": ""}, {"name": None, "description": ""}
	elif len(location_objects) == 1:
		location_object_1, location_object_2 = misc_objects[location_objects[0]], {"name": None, "description": ""}
	elif len(location_objects) == 2:
		location_object_1, location_object_2 = misc_objects[location_objects[0]], misc_objects[location_objects[1]]

	if len(location_entities) == 0:
		location_entity_1, location_entity_2 = {"name": None, "description": ""}, {"name": None, "description": ""}
	elif len(location_entities) == 1:
		location_entity_1, location_entity_2 = entities[location_entities[0]], {"name": None, "description": ""}
	elif len(location_entities) == 2:
		location_entity_1, location_entity_2 = entities[location_entities[0]], entities[location_entities[1]]

	os.system("clear")
	print(f"┏━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┓                ")
	print(f"┃  {CYAN}[ PUREYA ]{WHITE}  ┃ {GREEN}[HP] {hp}/100{WHITE} ┃ {RED}[ COMMS ] --{WHITE} ┃ {MAGENTA}[ {player.current_world_name.upper()} ]{WHITE} ┃ {BLUE}[ SETTINGS ]{WHITE} ┃                ")
	print(f"┣━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━╋━━━[ {YELLOW}YOROI{WHITE} ]━━━┓")
	print(f"┃ {YELLOW}┏" + (f"━" * (len(location_name) + 2)) + f"┓{WHITE}" + (f" " * (71 - (len(location_name) + 2))) + f"┃               ┃")
	print(f"┃ {YELLOW}┃ {location_name} ┃{WHITE}" + (f" " * (71 - (len(location_name) + 2))) + f"┃ {LIGHTGREEN_EX}[ HERUMETTO ]{WHITE} ┃")
	print(f"┃ {YELLOW}┣" + (f"━" * (len(location_name) + 2)) + f"┛{WHITE}" + (f" " * (71 - (len(location_name) + 2))) + f"┃     00/10     ┃")
	print(f"┃ {YELLOW}┣╸{WHITE}{line_1}" + (f" " * (71 - (len(line_1)))) + f"┃  {LIGHTGREEN_EX}[ MUNEATE ]{WHITE}  ┃")
	print(f"┃ {YELLOW}┣╸{WHITE}{line_2}" + (f" " * (71 - (len(line_2)))) + f"┃     00/10     ┃")
	print(f"┃ {YELLOW}┣╸{WHITE}{line_3}" + (f" " * (71 - (len(line_3)))) + f"┃  {LIGHTGREEN_EX}[ REGINSU ]{WHITE}  ┃")
	print(f"┃ {YELLOW}┗╸{WHITE}{line_4}" + (f" " * (71 - (len(line_4)))) + f"┃     00/10     ┃")
	print(f"┃   🮥  " + location_object_1["description"] + (f" " * (74 - (len(location_object_1["description"]) + 6))) + f"┃   {LIGHTGREEN_EX}[ BUTSU ]{WHITE}   ┃")
	print(f"┃   🮥  " + location_object_2["description"] + (f" " * (74 - (len(location_object_2["description"]) + 6))) + f"┃     00/10     ┃")
	print(f"┃   🮥  " + location_entity_1["description"] + (f" " * (74 - (len(location_entity_1["description"]) + 6))) + f"┃               ┃")
	print(f"┃   🮥  " + location_entity_2["description"] + (f" " * (74 - (len(location_entity_2["description"]) + 6))) + f"┣━━━[ {YELLOW}ZAIKO{WHITE} ]━━━┫")
	print(f"┃                                                                          ┃               ┃")
	print(f"┃ {MAGENTA}NORTH |{WHITE} " + north_location["name"] + (f" " * (29 - len(north_location["name"]))) + f"{MAGENTA}EAST |{WHITE} " + east_location["name"] + (f" " * (29 - len(east_location["name"]))) + f"┃               ┃")
	print(f"┃ {MAGENTA}SOUTH |{WHITE} " + south_location["name"] + (f" " * (29 - len(south_location["name"]))) + f"{MAGENTA}WEST |{WHITE} " + west_location["name"] + (f" " * (29 - len(west_location["name"]))) + f"┃               ┃")
	print(f"┃ {MAGENTA}NORTH-EAST |{WHITE} " + north_east_location["name"] + (f" " * (24 - len(north_east_location["name"]))) + f"{MAGENTA}NORTH-WEST |{WHITE} " + north_west_location["name"] + (f" " * (23 - len(north_west_location["name"]))) + f"┃               ┃")
	print(f"┃ {MAGENTA}SOUTH-EAST |{WHITE} " + south_east_location["name"] + (f" " * (24 - len(south_east_location["name"]))) + f"{MAGENTA}SOUTH-WEST |{WHITE} " + south_west_location["name"] + (f" " * (23 - len(south_west_location["name"]))) + f"┃               ┃")
	print(f"┃ {MAGENTA}UP |{WHITE} " + up_location["name"] + (f" " * (32 - len(up_location["name"]))) + f"{MAGENTA}DOWN |{WHITE} " + down_location["name"] + (f" " * (29 - len(down_location["name"]))) + f"┃               ┃")
	print(f"┃                                                                          ┃               ┃")
	print(f"┣━[ {YELLOW}ROGU{WHITE} ]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫               ┃")
	print(f"┃                                                                          ┃               ┃")
	print(f"┃ {BLUE}┏╸{WHITE}{examination_line_1}" + (f" " * (71 - (len(examination_line_1)))) + f"┃               ┃")
	print(f"┃ {BLUE}┗╸{WHITE}{examination_line_2}" + (f" " * (71 - (len(examination_line_2)))) + f"┃               ┃")
	print(f"┃ {GREEN}# {player.previous_input}{WHITE}", (f" " * (69 - len(player.previous_input))), f"┃               ┃")
	print(f"┃ {RED}# {player.previous_error}{WHITE}", (f" " * (69 - len(player.previous_error))), f"┃               ┃")
	print(f"┃                                                                          ┃               ┃")
	print(f"┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━┛")
	player.previous_error = ""
	player.Prompt()