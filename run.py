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
   
class task_loot:
    def __init__(self, name, classification):
        self.name = name
        self.classification = classification
       
    def get_name(self):
        return self.name

    def get_classification(self):
        return self.classification

class player:
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
inventory = []
items = []
task_items = []

Clothes = loot (1, "clothes", "utility")
Aeroplane_food = loot (2, "aeroplane_food", "food")
Cables = loot (3, "cables", "utility")
Scrap_metal = loot (4, "scrap_metal", "utility")
Bottle_of_water = loot (5, "bottle_of_water", "water")
Life_vest = loot (6, "life_vest", "utility")
Air_mask = loot (7, "air_mask", "utility")
Parachute= loot (8, "parachute", "shelter")
Lighter= loot (9, "lighter", "utility")
Cooking_utensils = loot (10, "cooking_utensils", "utility")

Water_source = task_loot ("water_source", "water")
Coconut = task_loot ("coconut", "food")
Shelter = task_loot ("shelter", "shelter")


if __name__ == "__main__":
    print ("CRASH Landing")
    intro.start()
    intro.how_to_play()
    
  