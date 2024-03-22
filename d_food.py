import random


def food_search():
    def food_search_1():
        print(
            "Sounds like you've got a rumbly in your tumbly and I don't think we have any honey to help you Pooh bear"
        )
        food_choice = input(
            "well looks like there are two places we can go\n"
            " 1.Jungle\n"
            " 2.Beach"
        )
        if food_choice == "1":
            print(
                "The Jungle? well even in deepest, darkest Peru they had marmalade I suppose\n"
                " You travel deeper into the Jungle on a search for food"
            )
        elif food_choice == "2":
            beach_food()
        else:
            print("input incorrect try again")
            food_search_1()

    def food_search_2():
        found_cave = input(
            "AS you travel further you come across a small cave\n"
            " 1.Approach the cave\n"
            " 2.Keep on the search for food, you don't want to get distracted"
        )
        if found_cave == "1":
            print(
                "As you approach the cave a cute, white rabbit hops out and begins to sniff around the entrance of the cave, Awwwwwww how cute!"
            )
        elif found_cave == "2":
            print("There is nothing here, well this sucks. Time to go to the Beach")
            beach_food()
        else:
            print("input incorrect try again")
            food_search_2()

    def food_search_3():
        Rabbit = input(
            "That rabbit is adorable you could give it a hug.... or catch it and eat it, it's your game.\n"
            " 1.It's adorable BUT its not food so off to look elsewhere\n"
            " 2. It looks pretty tasty lets get closer"
        )
        if Rabbit == "1":
            print(
                "As you start heading away from the cave you notice a lot of bones surrounding the mouth of the cave,"
                " this rabbit was not normal, lets head to the beach and away from that thing"
            )
            beach_food()
        elif Rabbit == "2":
            print(
                "You approach the rabbit and notice too late that its red beady eyes and terrifying teeth dripping in blood are coming right at you,"
                " shame you didn't have a holy hand grenade"
            )
        else:
            print("input incorrect try again")
            food_search_3()


def beach_food():
    print(
        "its a beautiful day the sun, the sea, shade from beautiful coconut trees.... wait coconuts? WE FOUND FOOD! but how to get it?"
    )

    """
    New function?
    wrap coconut_tree
    update options as we go
    add player options
    """

def coconut_tree():
    
    choices = ["1.Climb_Tree", "2.Throw_Rocks", "3.Shake_Tree"]
 
    while True:
        chance = random.randint(1, 10)
        if len(choices) == 1:
            chance = 1

        f = "xxx"

        for item in choices: 
            f += item + "\n"
            
        playerchoice= input(f) 

        if playerchoice == "1":
            if chance > 5:
                print("Fail")
                choices.remove("1.Climb_Tree")

        elif playerchoice == "2":
            if chance > 2:
                print("Fail")
                choices.remove("2.Throw_Rocks")

        elif playerchoice == "3":
            if chance > 6:
                print("Fail")
                choices.remove("3.Shake_Tree")

        
            
if __name__ == "__main__":
   coconut_tree()
