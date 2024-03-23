import a_intro as intro
import b_game_start as game_start
import c_water as Water
import d_food as food
import e_shelter as shelter
import f_final as final


class loot:
    def __init__(self, number, name,  classification):
        self.number = number
        self.name = name
        self.classification = classification

    def get_number(self):
        return self.number
    
    def get_name(self):
        return self.name

    def get_classification(self):
        return self.classification
    '''
    clothes
    aeroplane_food
    Cables (rope)
    sharp/ shiny metal
    Bottle of water
    Life vest
    Air mask_tubing
    Parachute
    Lighter
    Cooking_utensils 
'''


#class player:
    '''
    Name
    inventory
    life t/f
    how to play
    '''
    '''
    check inventory 
    check how to play
    set Name
    change Name
    get name
    lose the life

'''

if __name__ == "__main__":
   # print ("CRASH Landing")
    #intro.start()
    #intro.how_to_play()
    '''
    inventory code needs to go in player class
    '''
    inventory = []
    '''
    item - number, name, classification 
    '''
    banana = loot(1,"banana", "fruit")
    apple = loot(2, "apple", "fruit")
    '''
    append to add to list
    '''
    inventory.append(banana)
    inventory.append(apple)
    print(inventory)

    for item in inventory:
        print(item.name)












#name = input("Enter your name:")
#print("Hello"  +name+"!")
