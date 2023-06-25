import os
import sys

from src.scenes.dlc_screen import DlcScreen
from src.scenes.game_screen import GameScreen
from src.scenes.help_screen import HelpScreen

def TitleScreen(player, dlcs):
    os.system("clear")
    print(fr"┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
    print(fr"┃                         ___ _____ ___    _   _  _ ___  ___ ___                           ┃")
    print(fr"┃                        / __|_   _| _ \  /_\ | \| |   \| __|   \                          ┃")
    print(fr"┃                        \__ \ | | |   / / _ \| .` | |) | _|| |) |                         ┃")
    print(fr"┃                        |___/ |_| |_|_\/_/ \_\_|\_|___/|___|___/                          ┃")
    print(fr"┃                               __   _____ ___ ___ ___ ___                                 ┃")
    print(fr"┃                               \ \ / / _ \_ _/ __| __/ __|                                ┃")
    print(fr"┃                                \ V / (_) | | (__| _|\__ \                                ┃")
    print(fr"┃                                 \_/ \___/___\___|___|___/                                ┃")
    print(fr"┃                                                                                          ┃")
    print(fr"┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫")
    print(fr"┃                                                                                          ┃")
    print(fr"┃   ┏━━━━━━━━[ DLC ]━━━━━━━━┓   ┏━━━━━━━━━[ MENU ]━━━━━━━━━┓   ┏━━━━━━[ CREDITS ]━━━━━━┓   ┃")
    print(fr"┃   ┃                       ┃   ┃    ___ _      ___   __   ┃   ┃                       ┃   ┃")
    print(fr"┃   ┃  {dlcs[0].Active()} - World Builder    ┃   ┃   | _ \ |    /_\ \ / /   ┃   ┃                       ┃   ┃")
    print(fr"┃   ┃                       ┃   ┃   |  _/ |__ / _ \ V /    ┃   ┃                       ┃   ┃")
    print(fr"┃   ┃  {dlcs[1].Active()} - English Lover    ┃   ┃   |_| |____/_/ \_\_|     ┃   ┃                       ┃   ┃")
    print(fr"┃   ┃                       ┃   ┃    _  _ ___ _    ___     ┃   ┃                       ┃   ┃")
    print(fr"┃   ┃  {dlcs[2].Active()} - Redemption       ┃   ┃   | || | __| |  | _ \    ┃   ┃                       ┃   ┃")
    print(fr"┃   ┃                       ┃   ┃   | __ | _|| |__|  _/    ┃   ┃                       ┃   ┃")
    print(fr"┃   ┃  X -                  ┃   ┃   |_||_|___|____|_|      ┃   ┃                       ┃   ┃")
    print(fr"┃   ┃                       ┃   ┃    _____  _____ _____    ┃   ┃                       ┃   ┃")
    print(fr"┃   ┃  X -                  ┃   ┃   | __\ \/ /_ _|_   _|   ┃   ┃                       ┃   ┃")
    print(fr"┃   ┃                       ┃   ┃   | _| >  < | |  | |     ┃   ┃                       ┃   ┃")
    print(fr"┃   ┃  X -                  ┃   ┃   |___/_/\_\___| |_|     ┃   ┃                       ┃   ┃")
    print(fr"┃   ┃                       ┃   ┃                          ┃   ┃                       ┃   ┃")
    print(fr"┃   ┗━━━━━━━━━━━━━━━━━━━━━━━┛   ┗━━━━━━━━━━━━━━━━━━━━━━━━━━┛   ┗━━━━━━━━━━━━━━━━━━━━━━━┛   ┃")
    print(fr"┃                                                                                          ┃")
    print(fr"┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
    TitleScreenSelections(player, dlcs)


def TitleScreenSelections(player, dlcs):
    user_input = input("🮥🮥🮥 ")
    user_input = user_input.lower()
    while user_input not in ["play", "help", "exit", "dlc", "redemption"]:
        user_input = input("🮥🮥🮥 ")
        TitleScreen(player)
    if user_input == "play":
        GameScreen(player)
    elif user_input == "help":
        HelpScreen(player, dlcs)
    elif user_input == "exit":
        sys.exit()
    elif user_input == "dlc":
        DlcScreen(player, dlcs)
    elif user_input == "redemption":
        if dlcs[2].initialized == True:
            print("Accepted")
        else:
            print("That DLC is not initialized.")