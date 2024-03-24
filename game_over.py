import a_intro as intro


def game_over():
    """
    This function reads then prints the information from the .txt file in to the terminal
    """
    dead = "game_over.txt"
    with open(dead, "r") as file:
        # Read the content of the file
        file_content = file.read()


def play_again():
    play = input("play again? 1. yes\n 2. no\n")
    if play == "1":
        intro.start()

    elif play == "2":
        print("GAME OVER!\n See you next Time!")

    else:
        print("invalid entry")
        play_again()
