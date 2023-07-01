import os
import platform

from dlc.builder.world_builder import WorldBuilder
from dlc.english_lover.english_lover import EnglishLover
from dlc.redemption.redemption import Redemption
from dlc.xeon.xeon import Xeon

from src.classes.player import Player
from src.scenes.ui_screens.title_screen import TitleScreen
from src.utils.colors import *
from src.utils.constants import *


class Main:
	def __init__(self) -> None:
		self.title = "Stranded Voices"
		self.dlcs = [WorldBuilder(), EnglishLover(), Redemption(), Xeon()]
		self.player = Player()
		self.SCREEN_WIDTH = WIDTH
		self.SCREEN_HEIGHT = HEIGHT
		self.SetConsoleSize()


	def SetConsoleSize(self):
		if platform.system() == "Windows":
			os.system(f"title {self.title}")
			os.system(f"mode con: cols={self.SCREEN_WIDTH} lines={self.SCREEN_HEIGHT}")
		elif platform.system() == "Linux" or platform.system() == "Darwin":
			os.system(f"echo -n -e'\033]0;{self.title}\007'")
			os.system(f"echo '\033[8;{self.SCREEN_HEIGHT};{self.SCREEN_WIDTH}t'")


	def run(self) -> None:
		print(f"{WHITE}{BLACK_BG}")
		TitleScreen(self.player, self.dlcs)