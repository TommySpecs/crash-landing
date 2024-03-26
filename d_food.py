import random
import game_over as GO
from time import sleep as wait


def food_search_1():
    print(
        "Sounds like you've got a rumbly in your tumbly"
        " and I don't think we have any honey to help you Pooh bear\n"
    )
    wait(0.5)
    food_choice = input(
        "well looks like there are two places we can go\n"
        " 1.Jungle\n"
        " 2.Beach\n"
    )
    wait(0.5)
    if food_choice == "1":
        print(
            "The Jungle? well even in deepest, darkest Peru"
            " they had marmalade I suppose\n"
            " You travel deeper into the Jungle on a search for food\n"
        )
        wait(0.5)
        food_search_2()

    elif food_choice == "2":
        coconut_tree()
    else:
        print("input incorrect try again")
        food_search_1()
        wait(0.5)


def food_search_2():
    found_cave = input(
        "AS you travel further you come across a small cave\n"
        " 1.Approach the cave\n"
        " 2.Keep on the search for food, you don't want to get distracted\n"
    )
    wait(0.5)
    if found_cave == "1":
        print(
            "As you approach the cave a cute, white rabbit hops out"
            " and begins to sniff around the entrance of the cave,"
            " Awww how cute!\n"
        )
        wait(0.5)
        food_search_3()

    elif found_cave == "2":
        print("There is nothing here, this sucks. Time to go to the Beach")
        coconut_tree()
    else:
        print("input incorrect try again")
        food_search_2()
        wait(0.5)


def food_search_3():
    Rabbit = input(
        "That rabbit is adorable you could give it a hug.... or catch it"
        " and eat it, it's your game.\n"
        " 1.It's adorable BUT its not food so off to look elsewhere\n"
        " 2. It looks pretty tasty lets get closer\n"
    )
    wait(0.5)
    if Rabbit == "1":
        print(
            "As you start heading away from the cave you notice "
            "a lot of bones surrounding the mouth of the cave,"
            " this rabbit was not normal, "
            "lets head to the beach and away from that thing"
        )
        coconut_tree()
    elif Rabbit == "2":
        print(
            "You approach the rabbit and notice too late"
            " its red beady eyes and terrifying teeth dripping in blood"
            " are coming right at you,"
            " shame you didn't have a holy hand grenade"
        )
        GO.game_over()

    else:
        print("input incorrect try again")
        food_search_3()


def coconut_tree():
    print("its a beautiful day the sun, the sea, "
          "shade from beautiful coconut trees.... wait coconuts?"
          " WE FOUND FOOD! but how to get it?\n")
    wait(0.5)

    choices = ["1.Climb_Tree", "2.Throw_Rocks", "3.Shake_Tree"]

    while True:
        chance = random.randint(1, 10)
        if len(choices) == 1:
            chance = 1

        f = "\n"

        for item in choices:
            f += item + "\n"
        playerchoice = input(f)
        if playerchoice == "1" and "1.Climb_Tree" in choices:
            if chance > 5:
                print("Well that didn't work lets try something else")
                choices.remove("1.Climb_Tree")
                wait(0.5)
            else:
                break

        elif playerchoice == "2" and "2.Throw_Rocks" in choices:
            if chance > 2:
                print("nope not this time, try something else")
                choices.remove("2.Throw_Rocks")
                wait(0.5)
            else:
                break

        elif playerchoice == "3" and "3.Shake_Tree" in choices:
            if chance > 6:
                print("Darn! I so thought that would work, try something else")
                choices.remove("3.Shake_Tree")
                wait(0.5)
            else:
                break

        else:
            print("Please pick a valid response")

    end_food()


def end_food():
    print(
        "You got a coconut! A valuable resource has been secured. "
        "Congratulations\n")
    wait(0.5)
