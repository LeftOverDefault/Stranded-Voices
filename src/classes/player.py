import os
import sys

from src.entities.entities import entities
from src.scenes.game_screen import GameScreen, InteractScreen
from src.scripts.check_player_status import CheckPlayerStatus
from src.scripts.error import (DirectionError, InteractionError, LocationError,
                               PromptError)
from src.scripts.movement_handler import Move
from src.worlds.world_1 import world_1, world_name


class Player:
	def __init__(self) -> None:
		self.current_location = "crew_quarters_l"
		self.current_world = world_1
		self.current_world_name = world_name
		self.hp = 100
		self.alive = True
		self.helmet_points = 0
		self.chestplate_points = 0
		self.leggings_points = 0
		self.boots_points = 0
		self.previous_input = ""
		self.previous_error = ""
		self.last_interaction = ""


	def Prompt(self):
		CheckPlayerStatus(self)
		if self.alive != False:
			user_input = input("🮥🮥🮥 ")
			self.previous_input = user_input
			user_input = user_input.lower()
			prompts = ["go", "use", "sneak", "exit", "interact"]
			try:
				command, args = user_input.split(" ")
			except:
				command = user_input
				args = None
			while command not in prompts:
				self.previous_error = PromptError(self, user_input)
				GameScreen(self)
				self.Prompt()
			if command == "go":
				if args != None:
					move = Move(self, args)
					if move == "direction_error":
						self.previous_error = DirectionError(self, args)
						GameScreen(self)
						self.Prompt()
					elif move == "location_error":
						self.previous_error = LocationError(self, args)
						GameScreen(self)
						self.Prompt()
					else:
						GameScreen(self)
						self.Prompt()
				else:
					self.previous_error = DirectionError(self, args)
					GameScreen(self)
					self.Prompt()



			elif command == "interact":
				if args != None and entities[args]["met"] == False:
					InteractScreen(self, args)
					self.last_interaction = args
					self.InteractPrompt()
				elif args == None and entities[args]["met"] == True:
					pass
				else:
					self.previous_error = InteractionError(self, args)
					InteractScreen(self, args)
					self.last_interaction = args
					self.InteractPrompt()
					

			elif command == "exit":
				sys.exit()
		else:
			self.DeathSequence()
	

	def InteractPrompt(self):
		CheckPlayerStatus(self)
		if self.alive != False:
			user_input = input("🮥🮥🮥 ")
			user_input = user_input.lower()
			self.previous_input = user_input
			prompts = ["leave", "exit"]
			while user_input not in prompts:
				self.previous_error = PromptError(self, user_input)
				InteractScreen(self, self.last_interaction)
				self.InteractPrompt()
			if user_input == "leave":
				self.previous_error = "You left"
				GameScreen(self)
				self.Prompt()
			elif user_input == "exit":
				sys.exit()


	def DeathSequence(self):
		pass