import os

from src.entities.entities import entities
from src.objects.misc import misc_objects
from src.utils.colors import *
from src.scripts.npc_dialogue_handler import DialogueHandler


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
	print(f"┏━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┓                \n┃  {CYAN}[ PUREYA ]{WHITE}  ┃ {GREEN}[HP] {hp}/100{WHITE} ┃ {RED}[ COMMS ] --{WHITE} ┃ {MAGENTA}[ {player.current_world_name.upper()} ]{WHITE} ┃ {BLUE}[ SETTINGS ]{WHITE} ┃                \n┣━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━╋━━━[ {YELLOW}YOROI{WHITE} ]━━━┓\n┃ {YELLOW}┏" + (f"━" * (len(location_name) + 2)) + f"┓{WHITE}" + (f" " * (71 - (len(location_name) + 2))) + f"┃               ┃\n┃ {YELLOW}┃ {location_name} ┃{WHITE}" + (f" " * (71 - (len(location_name) + 2))) + f"┃ {LIGHTGREEN_EX}[ HERUMETTO ]{WHITE} ┃\n┃ {YELLOW}┣" + (f"━" * (len(location_name) + 2)) + f"┛{WHITE}" + (f" " * (71 - (len(location_name) + 2))) + f"┃     00/10     ┃\n┃ {YELLOW}┣╸{WHITE}{line_1}" + (f" " * (71 - (len(line_1)))) + f"┃  {LIGHTGREEN_EX}[ MUNEATE ]{WHITE}  ┃\n┃ {YELLOW}┣╸{WHITE}{line_2}" + (f" " * (71 - (len(line_2)))) + f"┃     00/10     ┃\n┃ {YELLOW}┣╸{WHITE}{line_3}" + (f" " * (71 - (len(line_3)))) + f"┃  {LIGHTGREEN_EX}[ REGINSU ]{WHITE}  ┃\n┃ {YELLOW}┗╸{WHITE}{line_4}" + (f" " * (71 - (len(line_4)))) + f"┃     00/10     ┃\n┃   🮥  " + location_object_1["description"] + (f" " * (74 - (len(location_object_1["description"]) + 6))) + f"┃   {LIGHTGREEN_EX}[ BUTSU ]{WHITE}   ┃\n┃   🮥  " + location_object_2["description"] + (f" " * (74 - (len(location_object_2["description"]) + 6))) + f"┃     00/10     ┃\n┃   🮥  " + location_entity_1["description"] + (f" " * (74 - (len(location_entity_1["description"]) + 6))) + f"┃               ┃\n┃   🮥  " + location_entity_2["description"] + (f" " * (74 - (len(location_entity_2["description"]) + 6))) + f"┣━━━[ {YELLOW}ZAIKO{WHITE} ]━━━┫\n┃                                                                          ┃               ┃\n┃ {MAGENTA}NORTH |{WHITE} " + north_location["name"] + (f" " * (29 - len(north_location["name"]))) + f"{MAGENTA}EAST |{WHITE} " + east_location["name"] + (f" " * (29 - len(east_location["name"]))) + f"┃               ┃\n┃ {MAGENTA}SOUTH |{WHITE} " + south_location["name"] + (f" " * (29 - len(south_location["name"]))) + f"{MAGENTA}WEST |{WHITE} " + west_location["name"] + (f" " * (29 - len(west_location["name"]))) + f"┃               ┃\n┃ {MAGENTA}NORTH-EAST |{WHITE} " + north_east_location["name"] + (f" " * (24 - len(north_east_location["name"]))) + f"{MAGENTA}NORTH-WEST |{WHITE} " + north_west_location["name"] + (f" " * (23 - len(north_west_location["name"]))) + f"┃               ┃\n┃ {MAGENTA}SOUTH-EAST |{WHITE} " + south_east_location["name"] + (f" " * (24 - len(south_east_location["name"]))) + f"{MAGENTA}SOUTH-WEST |{WHITE} " + south_west_location["name"] + (f" " * (23 - len(south_west_location["name"]))) + f"┃               ┃\n┃ {MAGENTA}UP |{WHITE} " + up_location["name"] + (f" " * (32 - len(up_location["name"]))) + f"{MAGENTA}DOWN |{WHITE} " + down_location["name"] + (f" " * (29 - len(down_location["name"]))) + f"┃               ┃\n┃                                                                          ┃               ┃\n┣━[ {YELLOW}ROGU{WHITE} ]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫               ┃\n┃                                                                          ┃               ┃\n┃ {BLUE}┏╸{WHITE}{examination_line_1}" + (f" " * (71 - (len(examination_line_1)))) + f"┃               ┃\n┃ {BLUE}┗╸{WHITE}{examination_line_2}" + (f" " * (71 - (len(examination_line_2)))) + f"┃               ┃\n┃ {GREEN}# {player.previous_input}{WHITE}", (f" " * (69 - len(player.previous_input))), f"┃               ┃\n┃ {RED}# {player.previous_error}{WHITE}", (f" " * (69 - len(player.previous_error))), f"┃               ┃\n┃                                                                          ┃               ┃\n┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━┛")
	player.previous_error = ""

def InteractScreen(player, interaction):
	hp = player.hp
	current_world = player.current_world
	current_location = player.current_location
	location_examination = current_world[current_location]["examination"]

	if location_examination == None:
		examination_line_1, examination_line_2 = "None", "None"
	else:
		examination_line_1, examination_line_2 = location_examination.split("\l")

	character = entities[interaction]
	character_name = character["name"]

	dialogue_1, response_1, response_2, response_3, response_4 = DialogueHandler(player, interaction)

	os.system("clear")
	print(f"┏━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┓                \n┃  {CYAN}[ PUREYA ]{WHITE}  ┃ {GREEN}[HP] {hp}/100{WHITE} ┃ {RED}[ COMMS ] --{WHITE} ┃ {MAGENTA}[ {player.current_world_name.upper()} ]{WHITE} ┃ {BLUE}[ SETTINGS ]{WHITE} ┃                \n┣━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━╋━━━[ {YELLOW}YOROI{WHITE} ]━━━┓\n┃ {YELLOW}┏" + (f"━" * (len(character_name) + 2)) + f"┓{WHITE}" + (f" " * (71 - (len(character_name) + 2))) + f"┃               ┃\n┃ {YELLOW}┃ {character_name} ┃{WHITE}" + (f" " * (71 - (len(character_name) + 2))) + f"┃ {LIGHTGREEN_EX}[ HERUMETTO ]{WHITE} ┃\n┃ {YELLOW}┣" + (f"━" * (len(character_name) + 2)) + f"┛{WHITE}" + (f" " * (71 - (len(character_name) + 2))) + f"┃     00/10     ┃\n┃                                                                          ┃  {LIGHTGREEN_EX}[ MUNEATE ]{WHITE}  ┃\n┃                                                                          ┃     00/10     ┃\n┃                                                                          ┃  {LIGHTGREEN_EX}[ REGINSU ]{WHITE}  ┃\n┃                                                                          ┃     00/10     ┃\n┃                                                                          ┃   {LIGHTGREEN_EX}[ BUTSU ]{WHITE}   ┃\n┃                                                                          ┃     00/10     ┃\n┃                                                                          ┃               ┃\n┃                                                                          ┣━━━[ {YELLOW}ZAIKO{WHITE} ]━━━┫\n┣━━[ {YELLOW}OPUSHONS{WHITE} ]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫               ┃\n┃                                                                          ┃               ┃\n┃ 1) {response_1}" + (f" " * (74 - (len(response_1) + 4))) + f"┃               ┃\n┃ 2) {response_2}" + (f" " * (74 - (len(response_2) + 4))) + f"┃               ┃\n┃ 3) {response_3}" + (f" " * (74 - (len(response_3) + 4))) + f"┃               ┃\n┃ 4) {response_4}" + (f" " * (74 - (len(response_4) + 4))) + f"┃               ┃\n┃                                                                          ┃               ┃\n┣━[ {YELLOW}ROGU{WHITE} ]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫               ┃\n┃                                                                          ┃               ┃\n┃ {BLUE}┏╸{WHITE}{examination_line_1}" + (f" " * (71 - (len(examination_line_1)))) + f"┃               ┃\n┃ {BLUE}┗╸{WHITE}{examination_line_2}" + (f" " * (71 - (len(examination_line_2)))) + f"┃               ┃\n┃ {GREEN}# {player.previous_input}{WHITE}", (f" " * (69 - len(player.previous_input))), f"┃               ┃\n┃ {RED}# {player.previous_error}{WHITE}", (f" " * (69 - len(player.previous_error))), f"┃               ┃\n┃                                                                          ┃               ┃\n┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━┛")
	player.previous_error = ""