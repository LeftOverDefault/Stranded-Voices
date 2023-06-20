from src.classes.npc import NPC


class Ellie(NPC):
	def __init__(self) -> None:
		super().__init__("ellie")
	
	def PrintDialogue(self):
		print(self.dialogue)