import random


def food_search ():
    def food_search_1():
        print("Sounds like you've got a rumbly in your tumbly and I don't think we have any honey to help you Pooh bear")
        food_choice = input("well looks like there are two places we can go\n 1.Jungle\n 2.Beach")
        if food_choice == "1":
            print("The Jungle? well even in deepest, darkest Peru they had marmalade I suppose\n You travel deeper into the Jungle on a search for food")
        elif food_choice =="2":
            beach_food()
        else:
            print("input incorrect try again")
            food_search_1()

    def food_search_2():
        found_cave = input("AS you travel further you come across a small cave\n 1.Approach the cave\n 2.Keep on the search for food, you don't want to get distracted")
        if found_cave == "1":
            print("As you approach the cave a cute, white rabbit hops out and begins to sniff around the enterance of the cave, Awwwwwww how cute!")
        elif found_cave == "2":
            print("There is nothing here, well this sucks. Time to go to the Beach")
            beach_food()
        else:
            print("input incorrect try again")
            food_search_2()

    def food_search_3():
        Rabbit = input("That rabbit is adorable you could give it a hug.... or catch it and eat it, it's your game.\n 1.It's adorable BUT its not food so off to look elsewhere\n 2. It looks pretty tasty lets get closer")
        if Rabbit == "1":
            print("As you start heading away from the cave you notice a lot of bones surronding the mouth of the cave, this rabbit was not normal, lets head to the beach and away from that thing")
            beach_food()
        elif Rabbit == "2":
            print("You appraoch the rabbit and notice too late that its red beady eyes and terrifying teeth dripping in blood are coming right at you, shame you didn't have a holy hand grenade")
        else:
            print("input incorrect try again")
            food_search_3()

def beach_food ():
    print("its a beautiful day the sun, the sea, shade from beautiful coconut trees.... wait coconuts? WE FOUND FOOD! but how to get it?")
    



    def coconut_tree():
        chance = random.randint(1,10)
        choices = ["Climb_Tree", "Throw_Rocks", "Shake_Tree"]
        
        with True:
            if choices == "Climb-Tree":
                if chance > 5:
                    print("Fail")
                    choices.remove ("Climb_Tree")       
                    
            elif choices == "Throw_Rocks":
                if chance > 2: 
                    print("Fail")
                    choices.remove ("Throw_Rocks")
                                
            elif choices == "Shake_Tree":
                if chance > 6: 
                    print("Fail")
                    choices.remove ("Shake_Tree")





"""
Climb = 40% success 4 in 10
Throw =  20% success 2 in 10
Shake tree=  50% success 5 in 10
         
hide each choice once chosen
auto success on last always

Beach
You see coconut trees
climb tree
throw rocks
shake tree
(each choise has a percentage of working after two fails tird must succeed)
"""