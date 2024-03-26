import c_water as water
import d_food as food
import e_shelter as shelter
import f_final as final
from time import sleep as wait
from colorama import Fore, Back, Style


def game_intro():
    """
    This function reads then prints the information from the
    .txt file in to the terminal
    """
    intro = "game_start_intro.txt"
    with open(intro, 'r') as startupFile:
        for line in startupFile:
            print(Fore.CYAN + line, end="")
            wait(0.5)
        print("\n")
        check()


def check():
    print(Fore.CYAN +
          "You are overwhelmed by everything that has happened,\n"
          "where are you?\n are you okay?\n well I guess your better check\n")
    wait(0.5)
    choice1 = input(Fore.CYAN + "Select 1 or 2\n"
                    " 1.Check for injuries\n" " 2.Check bearings\n")
    if choice1 == "1":
        print(Fore.CYAN +
              "You check yourself for any injuries\n"
              "By the grace of a great unknown force\n"
              " you are completely fine\n")
        wait(0.5)
        run_away()
    elif choice1 == "2":
        print(Fore.CYAN +
              "eye spy with my little eye something beginning with ummmm....\n"
              "a crashed plane, and a jungle....\n"
              " nope you have no idea where you are\n")
        wait(0.5)
        run_away()
    else:
        print("input incorrect try again")
        check()


def run_away():
    print(Fore.CYAN +
          "Well I guess you're now feeling \n"
          " a little better about your situation, maybe?\n"
          " no? oh well\n any way the strange scent of ash,\n"
          " flesh and\n the sweet sweet aroma of airplane peanuts"
          " fill the air\n")
    wait(0.5)
    choice2 = input(Fore.CYAN +
                    "oh look more choices, choose 1 or 2\n"
                    " 1.we all know wild animals love airplane peanuts\n"
                    " its a fact or something you could run away\n"
                    " 2.Hey there might be some useful stuff here \n"
                    " the other passengers don't need it anymore"
                    " search the wreckage\n")
    if choice2 == "1":
        print(Fore.CYAN +
              "Yeah its probably for the best,\n"
              " the corpses where giving me the heebie jeebies\n")
        wait(0.5)
        next_steps()
    elif choice2 == "2":
        print(Fore.CYAN +
              "oh look at you! you sweet sweet loot goblin,\n"
              " I am proud of you. You didn't find anything useful,\n"
              " but you tried\n")
        wait(0.5)
        next_steps()
    else:
        print("input incorrect try again")
        run_away()


def next_steps():
    print(Fore.CYAN + "All those years of watching survival programmes"
          " come back to you\n")
    wait(0.5)

    choices = ["1.water", "2.food", "3.shelter"]

    while True:

        f = "You remember you need to find:\n"

        for item in choices:
            f += item + "\n"

        playerchoice = input(f)

        if playerchoice == "1" and "1.water" in choices:
            water.water()
            choices.remove("1.water")

        elif playerchoice == "2" and "2.food" in choices:
            food.food_search_1()
            choices.remove("2.food")

        elif playerchoice == "3" and "3.shelter" in choices:
            shelter.shelter()
            choices.remove("3.shelter")

        else:
            print("Please pick a valid response")

        if len(choices) == 0:
            break
    final.finale()
