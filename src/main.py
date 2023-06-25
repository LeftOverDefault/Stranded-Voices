import os
import platform

from src.classes.player import Player
from src.scenes.game_screen import GameScreen
from src.scenes.title_screen import TitleScreen
from src.utils.colors import *

from dlc.builder.world_builder import WorldBuilder
from dlc.english_lover.english_lover import EnglishLover
from dlc.redemption.redemption import Redemption
from dlc.xeon.xeon import Xeon


class Main:
	def __init__(self) -> None:
		self.title = "Stranded Voices"
		self.dlcs = [WorldBuilder(), EnglishLover(), Xeon(), Redemption()]
		self.player = Player()
		self.SCREEN_WIDTH = 92
		self.SCREEN_HEIGHT = 30
		self.SetConsoleSize()



	def SetConsoleSize(self):
		if platform.system() == "Windows":
			os.system(f"title {self.title}")
			os.system("mode con: cols={} lines={}".format(self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
		elif platform.system() == "Linux" or platform.system() == "Darwin":
			os.system(f"echo -n -e'\033]0;{self.title}\007'")
			os.system("echo '\033[8;{};{}t'".format(self.SCREEN_HEIGHT, self.SCREEN_WIDTH))


	def run(self) -> None:
		print(f"{WHITE}{BLACK_BG}")
		TitleScreen(self.player, self.dlcs)