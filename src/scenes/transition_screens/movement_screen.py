import math
import os
import time

from src.objects.misc import misc_objects
from src.utils.colors import *


def MovementScreen(player, direction, old_location):
	old_location_name = player.current_world[old_location]["name"]
	location_name = player.current_world[player.current_location]["name"]

	descriptions = ["", "", "", ""]
	for i in range(len(player.current_world[old_location]["directions"][direction]["move_description"].split("\l"))):
		descriptions[i] = (player.current_world[old_location]["directions"][direction]["move_description"].split("\l"))[i]

	inventory = ["", "", "", "", "", "", "", "", "", "", "", "", ""]
	for i in range(len(player.inventory)):
		inventory[i] = misc_objects[player.inventory[i]]["name"]

	os.system("clear")
	print(fr"                                               ┏━━━━━━━━━━━━━━━━━┓                                               ")
	print(fr"┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫    {CYAN}[ BASHO ]{WHITE}    ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━[ {YELLOW}TASUKU{WHITE} ]━━━┓")
	print(fr"┃                                              ┗━━━━━━━━━━━━━━━━━┛                             ┃                ┃")
	print(fr"┃                                                                                              ┃                ┃")
	print(fr"┃   ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[ {YELLOW}FROM{WHITE} ]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓   ┃                ┃")
	print(fr"┃   ┃" + (fr" " * int(math.trunc((86 - len(old_location_name)) / 2))) + fr"{old_location_name}" + (fr" " * (int((86 - len(old_location_name) - 1) / 2) + 1)) + fr"┃   ┃                ┃")
	print(fr"┃   ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛   ┃                ┃")
	print(fr"┃                                                                                              ┃                ┃")
	print(fr"┃                                                                                              ┃                ┃")
	print(fr"┃   ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[ {YELLOW}TO{WHITE} ]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓   ┃                ┃")
	print(fr"┃   ┃" + (fr" " * int(math.trunc((86 - len(location_name)) / 2))) + fr"{location_name}" + (fr" " * (int((86 - len(location_name) - 1) / 2) + 1)) + fr"┃   ┃                ┃")
	print(fr"┃   ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛   ┃                ┃")
	print(fr"┃                                                                                              ┃                ┃")
	print(fr"┃                                                                                              ┃                ┃")
	print(fr"┃                                                                          ┏━━━━━[ {YELLOW}YOROI{WHITE} ]━━━━━┻━━━━━━━━━━━━━━━━┫")
	print(fr"┃                                                                          ┃                                    ┃")
	print(fr"┃                                                                          ┃ {BLUE}┏╸{WHITE}{inventory[0]}" + (" " * (36 - (len(inventory[0]) + 3))) + "┃")
	print(fr"┃                                                                          ┃ {BLUE}┣╸{WHITE}{inventory[1]}" + (" " * (36 - (len(inventory[1]) + 3))) + "┃")
	print(fr"┣━[ {YELLOW}SETSEMEI{WHITE} ]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫ {BLUE}┣╸{WHITE}{inventory[2]}" + (" " * (36 - (len(inventory[2]) + 3))) + "┃")
	print(fr"┃                                                                          ┃ {BLUE}┣╸{WHITE}{inventory[3]}" + (" " * (36 - (len(inventory[3]) + 3))) + "┃")
	print(fr"┃ {BLUE}┏╸{WHITE}" + fr"{descriptions[0]}" + (fr" " * (71 - (len(descriptions[0])))) + fr"┃ {BLUE}┣╸{WHITE}{inventory[4]}" + (" " * (36 - (len(inventory[4]) + 3))) + "┃")
	print(fr"┃ {BLUE}┣╸{WHITE}" + fr"{descriptions[1]}" + (fr" " * (71 - (len(descriptions[1])))) + fr"┃ {BLUE}┣╸{WHITE}{inventory[5]}" + (" " * (36 - (len(inventory[5]) + 3))) + "┃")
	print(fr"┃ {BLUE}┣╸{WHITE}" + fr"{descriptions[2]}" + (fr" " * (71 - (len(descriptions[2])))) + fr"┃ {BLUE}┣╸{WHITE}{inventory[6]}" + (" " * (36 - (len(inventory[6]) + 3))) + "┃")
	print(fr"┃ {BLUE}┗╸{WHITE}" + fr"{descriptions[3]}" + (fr" " * (71 - (len(descriptions[3])))) + fr"┃ {BLUE}┣╸{WHITE}{inventory[7]}" + (" " * (36 - (len(inventory[7]) + 3))) + "┃")
	print(fr"┃                                                                          ┃ {BLUE}┣╸{WHITE}{inventory[8]}" + (" " * (36 - (len(inventory[8]) + 3))) + "┃")
	print(fr"┣━[ {YELLOW}ROGU{WHITE} ]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫ {BLUE}┣╸{WHITE}{inventory[9]}" + (" " * (36 - (len(inventory[9]) + 3))) + "┃")
	print(fr"┃                                                                          ┃ {BLUE}┣╸{WHITE}{inventory[10]}" + (" " * (36 - (len(inventory[10]) + 3))) + "┃")
	print(fr"┃ {GREEN}# {player.previous_input}{WHITE}", (f" " * (69 - len(player.previous_input))), f"┃ {BLUE}┣╸{WHITE}{inventory[11]}" + (" " * (36 - (len(inventory[11]) + 3))) + "┃")
	print(fr"┃ {RED}# {player.previous_error}{WHITE}", (f" " * (69 - len(player.previous_error))), f"┃ {BLUE}┗╸{WHITE}{inventory[12]}" + (" " * (36 - (len(inventory[12]) + 3))) + "┃")
	print(fr"┃                                                                          ┃                                    ┃")
	print(fr"┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
	time.sleep(8)