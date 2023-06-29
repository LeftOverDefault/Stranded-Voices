import os


def DlcScreen(player, dlcs, title_screen):
    os.system("clear")
    print(fr"┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
    print(fr"┃                                      ___  _    ___                                       ┃")
    print(fr"┃                                     |   \| |  / __|                                      ┃")
    print(fr"┃                                     | |) | |_| (__                                       ┃")
    print(fr"┃                                     |___/|____\___|                                      ┃")
    print(fr"┃                                                                                          ┃")
    print(fr"┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫")
    print(fr"┃                                                                                          ┃")
    print(fr"┃   ┏━━━━━━━━[ DLC ]━━━━━━━━┓   ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓   ┃")
    print(fr"┃   ┃                       ┃   ┃ Type in the name of the DLC (shown on the left) that ┃   ┃")
    print(fr"┃   ┃  {dlcs[0].Active()} - World Builder    ┃   ┃ you would like to initialize. Initializing a DLC will┃   ┃")
    print(fr"┃   ┃                       ┃   ┃ allow you to play the content inside it. If the DLC  ┃   ┃")
    print(fr"┃   ┃  {dlcs[1].Active()} - English Lover    ┃   ┃ cannot be initialized then download it from the game ┃   ┃")
    print(fr"┃   ┃                       ┃   ┃ GitHub page, then place it into the dlc folder, then ┃   ┃")
    print(fr"┃   ┃  {dlcs[2].Active()} - Redemption       ┃   ┃ you will be able to play the DLC.                    ┃   ┃")
    print(fr"┃   ┃                       ┃   ┃                                                      ┃   ┃")
    print(fr"┃   ┃  {dlcs[3].Active()} - Xeon             ┃   ┃ If you have any problems with the DLC or would like  ┃   ┃")
    print(fr"┃   ┃                       ┃   ┃ to submit your own, open an issue or pull request on ┃   ┃")
    print(fr"┃   ┃  X -                  ┃   ┃ the Github page and I will get to it as quickly as I ┃   ┃")
    print(fr"┃   ┃                       ┃   ┃ can.                                                 ┃   ┃")
    print(fr"┃   ┃  X -                  ┃   ┃                                                      ┃   ┃")
    print(fr"┃   ┃                       ┃   ┃ Note: The first four DLCs to be added will be shown  ┃   ┃")
    print(fr"┃   ┃  X -                  ┃   ┃ In this sidebar, all others will be given an         ┃   ┃")
    print(fr"┃   ┃                       ┃   ┃ identifier, which will have to be known by the player┃   ┃")
    print(fr"┃   ┃  X -                  ┃   ┃ and typed into this screen to be initialized.        ┃   ┃")
    print(fr"┃   ┃                       ┃   ┃ (I am a little bit limited for space here!)          ┃   ┃")
    print(fr"┃   ┗━━━━━━━━━━━━━━━━━━━━━━━┛   ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛   ┃")
    print(fr"┃                                                                                          ┃")
    print(fr"┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
    DlcScreenSelections(player, dlcs, title_screen)


def DlcScreenSelections(player, dlcs, title_screen):
    user_input = input("🮥🮥🮥 ")
    user_input = user_input.lower()
    while user_input not in ["back", "world-builder", "english-lover", "xeon", "redemption"]:
        DlcScreen(player, dlcs, title_screen)
        user_input = input("🮥🮥🮥 ")
    if user_input == "back":
        title_screen(player, dlcs)
    elif user_input == "world-builder":
        dlcs[0].initialized = not dlcs[0].initialized
        DlcScreen(player, dlcs, title_screen)
    elif user_input == "english-lover":
        dlcs[1].initialized = not dlcs[1].initialized
        DlcScreen(player, dlcs, title_screen)
    elif user_input == "redemption":
        dlcs[2].initialized = not dlcs[2].initialized
        DlcScreen(player, dlcs, title_screen)
    elif user_input == "xeon":
        dlcs[3].initialized = not dlcs[3].initialized
        DlcScreen(player, dlcs, title_screen)