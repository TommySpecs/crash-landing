from colorama import Fore
def game_over():
    """
    This function reads then prints the information from the .txt file in to the terminal
    """
    dead = "game_over.txt"
    with open(dead, "r") as file:
        # Read the content of the file
        file_content = file.read()
        print(Fore.RED + file_content)
    exit()