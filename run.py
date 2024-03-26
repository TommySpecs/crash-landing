import a_intro as intro
import b_game_start as game
from time import sleep as wait
from colorama import Fore, Back, Style


def title():
    """
    This function reads then prints the information from the
    .txt file in to the terminal
    """
    title = "title.txt"
    with open(title, "r") as startupFile:
        for line in startupFile:
            print(Fore.CYAN +  line, end="")
            wait(0.5)
        print("\n")

if __name__ == "__main__":
    title()
    intro.start()
    intro.how_to_play()
    game.game_intro()
