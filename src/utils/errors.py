from src.utils.colors import *


# * Error for a Location, for invalid locations
def LocationError(player, direction):
	error = f"You can't go \"{direction}\"."
	return error

# * Error for a Direction, for invalid directions
def DirectionError(player, direction):
	if direction != None and direction != "":
		error = f"There is no direction called \"{direction}\"."
	else:
		error = f"You can't go nowhere."
	return error

# * Error for a Prompt, for invalid player prompt
def PromptError(player, prompt):
	error = f"You can't \"{prompt}\"."
	return error

# * Error for an Interaction, for invalid player interaction with an npc
def InteractionError(player):
	error = f"You cannot interact with \"{player.last_interaction}\"."
	return error

# * Error for Dialogue, for invalid inputs when engaged in dialogue
def DialogueError(player):
	error = f"You have to choose a way to respond to {player.last_interaction}."
	return error

# * Error for Placing Objects, for invalid location of a placed object
def PlaceObjectError(player, object):
	if object != None:
		error = f"You can't place \"{object}\"."
	else:
		error = f"You can't place nothing."
	return error

# * Error for the player Inventory, for when a desired item is not in the player's inventory
def NotInInventoryError(player, object):
	error = f"There is no \"{object}\" in your inventory."
	return error

# * Error for an object Location, for when a player desires an object that is not in the room
def NotInLocationError(player, object):
	error = f"There is no \"{object}\" here."
	return error

# * Error for Inventory Space, for when the player tries to take or remove an object with no space left in the inventory
def InventorySpaceError(player):
	error = f"There is not enough space in your inventory for that."
	return error

# * Error for Removal of an Object, for when an object cannot be removed due to an invalid input
def RemoveObjectError(player, object):
	if object != None:
		error = f"You can't remove the \"{object}\"."
	else:
		error = f"You can't remove nothing."
	return error

# * Error for Taking an Object, for when an object cannot be taken due to an invalid input
def TakeObjectError(player, object):
	if object != None:
		error = f"You can't take the \"{object}\"."
	else:
		error = f"You can't take nothing."
	return error

# * Error for Space in a Location, for when an object is placed or dropped when no space is left for items at the location
def LocationSpaceError(player, object):
	error = f"There isn't enough space to place the \"{object}\"."
	return error

# * Error for an Object's Existence, for when the user input is invalid and so the object does not exist
def ObjectNotExistsError(player, object):
	error = f"There is no object named \"{object}\""
	return error