import game_over as GO
from time import sleep as wait


def shelter():
    print(
        "Well you need a place to sleep and protect you from the elements\n"
        " maybe a nice comfy shelter would do the trick\n")
    wait(0.5)
    choice_shelter1 = input(
        "While wandering through the jungle"
        " you start finding a good collection of sticks and large leaves,\n"
        " hey look there are a few in a pile here\n"
        " 1.add it to your collection\n"
        " 2.check it\n"
    )
    wait(0.5)
    if choice_shelter1 == "1":
        print(
            "well done champ your pile of sticks just grew\n"
            " hey! one of those sticks isn't a stick\n"
            " ....there is a venomous snake in the bundle,\n"
            " it bites you you die game over\n"
        )
        GO.game_over()

    elif choice_shelter1 == "2":
        print(
            "using your keen senses and glorious eyesight, "
            "those sticks look sturdy and perfect for you need\n"
            " Congratulations\n"
            " you use your gathered materials and make a shelter\n")
        wait(0.5)
        end_shelter()
    else:
        print("input incorrect try again")
        shelter()


def end_shelter():
    print(
        "You made a shelter! A valuable resource has been secured!"
        " Congratulations\n")
    wait(0.5)
