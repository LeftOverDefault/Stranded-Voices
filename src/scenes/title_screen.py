import os
import sys

from src.scenes.game_screen import GameScreen
from src.scenes.help_screen import HelpScreen


def TitleScreen(player):
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
    print(fr"┃                            ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓                               ┃")
    print(fr"┃                            ┃   ___ _____ _   ___ _____   ┃                               ┃")
    print(fr"┃                            ┃  / __|_   _/_\ | _ \_   _|  ┃                               ┃")
    print(fr"┃                            ┃  \__ \ | |/ _ \|   / | |    ┃                               ┃")
    print(fr"┃                            ┃  |___/ |_/_/ \_\_|_\ |_|    ┃                               ┃")
    print(fr"┃                            ┃      _  _ ___ _    ___      ┃                               ┃")
    print(fr"┃                            ┃     | || | __| |  | _ \     ┃                               ┃")
    print(fr"┃                            ┃     | __ | _|| |__|  _/     ┃                               ┃")
    print(fr"┃                            ┃     |_||_|___|____|_|       ┃                               ┃")
    print(fr"┃                            ┃    ___  _   _ ___ _____     ┃                               ┃")
    print(fr"┃                            ┃   / _ \| | | |_ _|_   _|    ┃                               ┃")
    print(fr"┃                            ┃  | (_) | |_| || |  | |      ┃                               ┃")
    print(fr"┃                            ┃   \__\_\\___/|___| |_|      ┃                               ┃")
    print(fr"┃                            ┃                             ┃                               ┃")
    print(fr"┃                            ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛                               ┃")
    print(fr"┃                                                                                          ┃")
    print(fr"┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
    TitleScreenSelections(player)


def TitleScreenSelections(player):
    user_input = input("🮥🮥🮥 ")
    user_input = user_input.lower()
    while user_input not in ["start", "help", "quit"]:
        user_input = input("🮥🮥🮥 ")
        TitleScreen(player)
    if user_input == "start":
        GameScreen(player)
    elif user_input == "help":
        HelpScreen(player)
    elif user_input == "quit":
        sys.exit()