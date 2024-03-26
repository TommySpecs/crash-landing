import game_over as GO
from time import sleep as wait


def water():
    print(
        "Feeling thirsty? yeah same,\n all that screaming during the crash"
        " really dried out your throat")
    wait(0.5)
    choice_water1 = input(
        "While looking for a water source in the jungle\n"
        " you hear a rustling in the bushes it could be a tasty snack?\n"
        " 1.investigate the bushes\n"
        " 2.Lets not get distracted we can find snacks later\n"
    )
    wait(0.5)
    if choice_water1 == "1":
        print(
            "oh you curious little thing, what could possible go...\n"
            " you have startled a wild boar and it's young.\n"
            " The wild boar savagely attacks you"
            " killing you and bringing our game to an end")
        wait(0.5)
        GO.game_over()
    elif choice_water1 == "2":
        print(
            "Well done you, you're able to focus on one task at a time\n"
            " as a reward the stream is just over here\n")
        wait(0.5)
        end_water()
    else:
        print("input incorrect try again")
        water()


def end_water():
    print(
        "You find the stream! A valuable resource has been secured."
        " Congratulations\n")
    wait(0.5)
