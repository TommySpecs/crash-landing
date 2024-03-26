from colorama import Fore, Back, Style


def start():
    """
    This function takes the user input start to start the game
    """
    user_input = input(Fore.CYAN + "Are you ready for your adventure?\n"
                       "type 'yes' to continue\n")
    if user_input == "yes":
        pass
    else:
        start()


def how_to_play():
    """
    This function reads then prints the information from the
    .txt file in to the terminal
    """
    h2p = "how_to_play.txt"
    with open(h2p, "r") as file:
        # Read the content of the file
        file_content = file.read()

        # Print the content
        print(
            Fore.YELLOW + "How To Play:",
            file_content,
            Style.RESET_ALL,
            sep="\n",
        )
