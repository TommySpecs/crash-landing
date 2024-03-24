global user_input
import b_game_start as game_start


def start():
    """
    This function takes the user input start to start the game
    """
    user_input = input("Please type start to play the game:")
    if user_input == "start":
        pass
    else:
        start()


def how_to_play():
    """
    This function reads then prints the information from the .txt file in to the terminal
    """
    h2p = "how_to_play.txt"
    with open(h2p, "r") as file:
        # Read the content of the file
        file_content = file.read()

        # Print the content
        print("how to play:\n", file_content)
        game_start.game_intro ()


