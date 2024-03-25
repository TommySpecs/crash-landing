import a_intro as intro
import b_game_start as game_start
import c_water as Water
import d_food as food
import e_shelter as shelter
import f_final as final


def title():
    """
    This function reads then prints the information from the .txt file in to the terminal
    """
    title = "title.txt"
    with open(title, "r") as file:
        # Read the content of the file
        file_content = file.read()

        # Print the content
        print(file_content)
        

if __name__ == "__main__":
    title()
    intro.start()
    intro.how_to_play()

  