import d_food as food
import e_shelter as shelter


def water():
    print(
        "Feeling thirsty? yay same all that screaming during the crash really dried out your throat"
    )
    choice_water1 = input(
        "While looking for a water source in the jungle you hear a rustling in the bushes it could be a tasty snack?\n"
        " 1.investigate the bushes\n"
        " 2.Lets not get distracted we can find snacks later\n"
    )
    if choice_water1 == "1":
        print(
            "oh you curious little thing, what could possible go........ you have startled a wild boar and it's young."
            " The wild boar savagely attacks you killing you and bringing our game to an end"
        )
    elif choice_water1 == "2":
        print(
            "Well done you you're able to focus on one task at a time as a reward the stream is just over here,"
        )
        end_water()
    else:
        print("input incorrect try again")
        water()


def end_water():
    print(
        "You find the stream and a valuable resource has been secured congratulations\n"
    )