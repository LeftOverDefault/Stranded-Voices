from src.utils.colors import *


def LocationError(player, direction):
	error = f"You can't go \"{direction}\"."
	return error

def DirectionError(player, direction):
	if direction != None and direction != "":
		error = f"There is no direction called \"{direction}\"."
	else:
		error = f"You can't go nowhere."
	return error
	
def PromptError(player, prompt):
	error = f"You can't \"{prompt}\"."
	return error

def InteractionError(player):
	error = f"You cannot interact with \"{player.last_interaction}\"."
	return error