import random

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

'''
    Name
    inventory
    how to play
    '''
    '''
    check inventory 
    check how to play
  '''
class player:
    def __init__(self, inventory, life,  how_to_play):
        self.inventory = inventory
        self.life = life
        self.how_to_play = how_to_play

    inventory = []

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

    def add_item(self, item):
        self.inventory.add(item)

    def add_task_item(self, task_item):
       self.inventory.add(task_item)

    def search_items():
       loot.number == random.randint(1,10)



       item_1 = random.randint(1, 10)
       player.inventory.add()