import os

from src.utils.colors import *

def InteractScreen(player, npc, npc_text, responses):
	hp = player.hp
	current_world = player.current_world
	current_location = player.current_location
	location_examination = current_world[current_location]["examination"]

	if location_examination == None:
		examination_line_1, examination_line_2 = "None", "None"
	else:
		examination_line_1, examination_line_2 = location_examination.split("\l")
	
	npc_name = npc["name"]
	
	try:
		response_1 = responses[0]
	except:
		response_1 = ""
	try:
		response_2 = responses[1]
	except:
		response_2 = ""
	try:
		response_3 = responses[2]
	except:
		response_3 = ""
	try:
		response_4 = responses[3]
	except:
		response_4 = ""

	os.system("clear")
	print(f"┏━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┓                ")
	print(f"┃  {CYAN}[ PUREYA ]{WHITE}  ┃ {GREEN}[HP] {hp}/100{WHITE} ┃ {RED}[ COMMS ] --{WHITE} ┃ {MAGENTA}[ {player.current_world_name.upper()} ]{WHITE} ┃ {BLUE}[ SETTINGS ]{WHITE} ┃                ")
	print(f"┣━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━╋━━━[ {YELLOW}YOROI{WHITE} ]━━━┓")
	print(f"┃ {YELLOW}┏" + (f"━" * (len(npc_name) + 2)) + f"┓{WHITE}" + (f" " * (71 - (len(npc_name) + 2))) + f"┃               ┃")
	print(f"┃ {YELLOW}┃ {npc_name} ┃{WHITE}" + (f" " * (71 - (len(npc_name) + 2))) + f"┃ {LIGHTGREEN_EX}[ HERUMETTO ]{WHITE} ┃")
	print(f"┃ {YELLOW}┣" + (f"━" * (len(npc_name) + 2)) + f"┛{WHITE}" + (f" " * (71 - (len(npc_name) + 2))) + f"┃     00/10     ┃")
	print(f"┃ {YELLOW}┗╸{WHITE}{npc_text}" + (f" " * (71 - (len(npc_text)))) + f"┃  {LIGHTGREEN_EX}[ MUNEATE ]{WHITE}  ┃")
	print(f"┃                                                                          ┃     00/10     ┃")
	print(f"┃                                                                          ┃  {LIGHTGREEN_EX}[ REGINSU ]{WHITE}  ┃")
	print(f"┃                                                                          ┃     00/10     ┃")
	print(f"┃                                                                          ┃   {LIGHTGREEN_EX}[ BUTSU ]{WHITE}   ┃")
	print(f"┃                                                                          ┃     00/10     ┃")
	print(f"┃                                                                          ┃               ┃")
	print(f"┃                                                                          ┣━━━[ {YELLOW}ZAIKO{WHITE} ]━━━┫")
	print(f"┣━━[ {YELLOW}OPUSHONS{WHITE} ]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫               ┃")
	print(f"┃                                                                          ┃               ┃")
	print(f"┃ 1) {response_1}" + (f" " * (74 - (len(response_1) + 4))) + f"┃               ┃")
	print(f"┃ 2) {response_2}" + (f" " * (74 - (len(response_2) + 4))) + f"┃               ┃")
	print(f"┃ 3) {response_3}" + (f" " * (74 - (len(response_3) + 4))) + f"┃               ┃")
	print(f"┃ 4) {response_4}" + (f" " * (74 - (len(response_4) + 4))) + f"┃               ┃")
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