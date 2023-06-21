import sys

from src.scenes.game_screen import GameScreen
from src.entities.entities import entities
from src.scripts.error import PromptError
from src.scenes.game_screen import InteractScreen


def DialogueHandler(player, npc_entity):
	current_dialogue = player.dialogue_index
	npc = entities[npc_entity]
	dialogue = npc["dialogue"][current_dialogue]

	npc_text, responses = dialogue.split(" ~ ")
	split_responses = [x.strip() for x in responses.split(" | ")]

	last_dialogue_option = list(npc["dialogue"].keys())[-1]

	if entities[npc_entity]["type"] == "regular" and entities[npc_entity]["met"] == False:
		print(npc_text)
		print(split_responses)

		user_input = str(input("🮥🮥🮥 "))
		player.previous_input = user_input
		user_input = user_input.lower()
		prompts = ["leave", "exit", "1", "2", "3", "4"]
		while user_input not in prompts:
			print("Please Choose an option")
			user_input = str(input("🮥🮥🮥 "))
		if user_input == "leave":
			player.previous_error = "You left"
			GameScreen(player)
			player.Prompt()
		elif user_input == "exit":
			sys.exit()
		elif user_input == "1":
			if len(player.dialogue_index) == len(last_dialogue_option):
				entities[npc_entity]["met"] = True
				player.previous_error = "You left"
				GameScreen(player)
				player.Prompt()
			else:
				player.dialogue_index += ".1"
				player.InteractPrompt()
		elif user_input == "2":
			if len(player.dialogue_index) == len(last_dialogue_option):
				entities[npc_entity]["met"] = True
				player.previous_error = "You left"
				GameScreen(player)
				player.Prompt()
			else:
				player.dialogue_index += ".2"
				player.InteractPrompt()
	elif entities[npc_entity]["type"] == "regular" and entities[npc_entity]["met"] == True:
		print(entities[npc_entity]["name"].title(), "doesn't want to talk to you.")
	elif entities[npc_entity]["type"] == "merchant":
		pass



	"""
			if user_input == "1":
				DialogueHandler(self, self.last_interaction)
			elif user_input == "2":
				print("input = 2")
	"""