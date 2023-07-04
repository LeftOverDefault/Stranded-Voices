import os
import sys

from src.entities.entities import entities
from src.scenes.game_screens.game_screen import GameScreen
from src.scripts.checks.check_game_status import CheckGameStatus
from src.scripts.checks.check_object_location_status import CheckObjectStatus
from src.scripts.checks.check_player_status import CheckPlayerStatus
from src.scripts.handlers.movement_handler import MovementHandler
from src.scripts.handlers.npc_dialogue_handler import DialogueHandler
from src.scripts.handlers.object_drop_handler import DropHandler
from src.scripts.handlers.object_placement_handler import PlacementHandler
from src.scripts.handlers.object_remove_handler import RemovalHandler
from src.scripts.handlers.object_take_handler import TakeHandler
from src.utils.errors import DirectionError, InteractionError, LocationError, PromptError, PlaceObjectError, RemoveObjectError, TakeObjectError, DropObjectError


class Player:
    def __init__(self) -> None:
        self.current_location = None
        self.current_world = None
        self.hp = 100
        self.alive = True
        self.inventory = []
        self.inventory_size = 13
        self.previous_input = ""
        self.previous_error = ""
        self.last_interaction = ""
        self.dialogue_index = "0"
        self.comms_established = False


    def Prompt(self):
        CheckGameStatus(self)
        CheckObjectStatus(self)
        CheckPlayerStatus(self)
        if self.alive != False:
            user_input = input("🮥🮥🮥 ")
            self.previous_input = user_input
            user_input = user_input.lower()
            prompts = ["go", "interact", "take", "drop", "place", "remove", "exit"]
            try:
                command, args = user_input.split(" ")
            except:
                command = user_input
                args = None
            while command not in prompts:
                self.previous_error = PromptError(self, user_input)
                GameScreen(self)
            if command == "go":
                if args != None:
                    self.last_interaction = args
                    MovementHandler(self, args)
                else:
                    self.previous_error = DirectionError(self, args)
                    GameScreen(self)
            elif command == "interact":
                if args != None:
                    self.last_interaction = args
                    self.InteractPrompt()
                else:
                    self.previous_error = InteractionError(self)
                    self.last_interaction = args
                    self.InteractPrompt()
            elif command == "take":
                if args != None:
                    TakeHandler(self, args)
                    GameScreen(self)
                else:
                    self.previous_error = TakeObjectError(self, args)
                    GameScreen(self)
            elif command == "drop":
                if args != None:
                    DropHandler(self, args)
                    GameScreen(self)
                else:
                    self.previous_error = DropObjectError(self, args)
                    GameScreen(self)
            elif command == "place":
                if args != None:
                    PlacementHandler(self, args)
                    GameScreen(self)
                else:
                    self.previous_error = PlaceObjectError(self, args)
                    GameScreen(self)
            elif command == "remove":
                if args != None:
                    RemovalHandler(self, args)
                    GameScreen(self)
                else:
                    self.previous_error = RemoveObjectError(self, args)
                    GameScreen(self)
            elif command == "exit":
                sys.exit()
        else:
            self.DeathSequence()


    def InteractPrompt(self):
        CheckPlayerStatus(self)
        if self.alive != False:
            while self.last_interaction not in entities.keys():
                self.previous_error = InteractionError(self)
                GameScreen(self)
            DialogueHandler(self, self.last_interaction)


    def DeathSequence(self):
        pass
