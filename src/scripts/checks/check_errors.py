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

def DialogueError(player):
	error = f"You have to choose a way to respond to {player.last_interaction}."
	return error

def PlaceObjectError(player, object):
	if object != None:
		error = f"You can't place \"{object}\"."
	else:
		error = f"You can't place nothing."
	return error

def PlaceLocationError(player, object):
	error = f"There is nowhere to place the \"{object}\"."
	return error

def NotInInventoryError(player, object):
	error = f"There is no \"{object}\" in your inventory."
	return error

def InventorySpaceError(player):
	error = f"There is not enough space in your inventory for that."
	return error

def RemoveObjectError(player, object):
	if object != None:
		error = f"You can't remove the \"{object}\"."
	else:
		error = f"You can't remove nothing."
	return error

def TakeObjectError(player, object):
	if object != None:
		error = f"You can't take the \"{object}\"."
	else:
		error = f"You can't take nothing."
	return error