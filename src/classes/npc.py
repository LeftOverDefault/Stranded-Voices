from src.entities.entities import entities


class NPC:
	def __init__(self, identifier) -> None:
		self.dict = entities
		self.name = entities[identifier]["name"]
		self.description = entities[identifier]["description"]
		self.met = entities[identifier]["met"]
		self.dialogue = entities[identifier]["dialogue"]
		self.art = entities[identifier]["art"]