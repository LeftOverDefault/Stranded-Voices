from src.entities.entities import entities

def DialogueHandler(player, npc):
    npc = entities[npc]
    dialogue = npc["dialogue"]
    dialogue_1 = dialogue["1"]["dialogue"]
    response_1 = dialogue["1"]["response_1"]
    response_2 = dialogue["1"]["response_2"]
    response_3 = dialogue["1"]["response_3"]
    response_4 = dialogue["1"]["response_4"]

    return dialogue_1, response_1, response_2, response_3, response_4