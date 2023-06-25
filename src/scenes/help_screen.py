import os
import sys


def HelpScreen(player, dlcs, title_screen):
    os.system("clear")
    print(fr"┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
    print(fr"┃                                    _  _ ___ _    ___                                     ┃")
    print(fr"┃                                   | || | __| |  | _ \                                    ┃")
    print(fr"┃                                   | __ | _|| |__|  _/                                    ┃")
    print(fr"┃                                   |_||_|___|____|_|                                      ┃")
    print(fr"┃                                                                                          ┃")
    print(fr"┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫")
    print(fr"┃ ┏━━━━━━━━━━[ DLC ]━━━━━━━━━━┓ ┏━━━━━━━━━━━━━━━━━━━━━━━━[ GAME ]━━━━━━━━━━━━━━━━━━━━━━━━┓ ┃")
    print(fr"┃ ┃ In order to initialize a  ┃ ┃                                                        ┃ ┃")
    print(fr"┃ ┃ DLC, return to the title  ┃ ┃                                                        ┃ ┃")
    print(fr"┃ ┃ screen menu and type in   ┃ ┃                                                        ┃ ┃")
    print(fr"┃ ┃ \"dlc\", to get to the dlc┃ ┃                                                        ┃ ┃")
    print(fr"┃ ┃ menu, there you enable or ┃ ┃                                                        ┃ ┃")
    print(fr"┃ ┃ disable DLCs to your      ┃ ┃                                                        ┃ ┃")
    print(fr"┃ ┃ liking.                   ┃ ┃                                                        ┃ ┃")
    print(fr"┃ ┃                           ┃ ┃                                                        ┃ ┃")
    print(fr"┃ ┃ If you would like to make ┃ ┃                                                        ┃ ┃")
    print(fr"┃ ┃ your very own dlc, please ┃ ┃                                                        ┃ ┃")
    print(fr"┃ ┃ feel free to open a ticket┃ ┃                                                        ┃ ┃")
    print(fr"┃ ┃ on the game's GitHub page.┃ ┃                                                        ┃ ┃")
    print(fr"┃ ┃                           ┃ ┃                                                        ┃ ┃")
    print(fr"┃ ┃ If you contribute to the  ┃ ┃                                                        ┃ ┃")
    print(fr"┃ ┃ project then your name    ┃ ┃                                                        ┃ ┃")
    print(fr"┃ ┃ will be added to the      ┃ ┃                                                        ┃ ┃")
    print(fr"┃ ┃ credit section in the menu┃ ┃                                                        ┃ ┃")
    print(fr"┃ ┃ only some will fit so     ┃ ┃                                                        ┃ ┃")
    print(fr"┃ ┃ there is a command for it.┃ ┃                                                        ┃ ┃")
    print(fr"┃ ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━┛ ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛ ┃")
    print(fr"┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
    HelpScreenSelections(player, dlcs, title_screen)


def HelpScreenSelections(player, dlcs, title_screen):
    user_input = input("🮥🮥🮥 ")
    user_input = user_input.lower()
    while user_input not in ["back", "exit"]:
        user_input = input("🮥🮥🮥 ")
        HelpScreen(player)
    if user_input == "back":
        title_screen(player, dlcs)
    elif user_input == "exit":
        sys.exit()