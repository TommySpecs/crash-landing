from colorama import Fore
from time import sleep as wait


def finale():
    """
    This function reads then prints the information from the
    .txt file in to the terminal
    """
    final = "final.txt"
    with open(final, 'r') as startupFile:
        for line in startupFile:
            print(Fore.YELLOW + line, end="")
            wait(0.5)
        print("\n")
    exit()
