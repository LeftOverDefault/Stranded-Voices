import os
import sys

from src.scenes.game_screen import GameScreen
from src.scripts.check_player_status import CheckPlayerStatus
from src.scripts.error import DirectionError, LocationError, PromptError
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


	def Prompt(self):
		CheckPlayerStatus(self)
		if self.alive != False:
			user_input = input("🮥🮥🮥  ")
			self.previous_input = user_input
			user_input = user_input.lower()
			prompts = ["go", "use", "sneak", "exit"]
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
			elif command == "exit":
				sys.exit()
		else:
			self.DeathSequence()


	def DeathSequence(self):
		pass