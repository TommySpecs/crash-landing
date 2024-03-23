import c_water as water
import d_food as food
import e_shelter as shelter



def game_intro ():
    '''
   This function reads then prints the information from the .txt file in to the terminal
    '''
    with open('game_start_intro.txt', 'r') as file:
     # Read the content of the file
        file_content = file.read()
            
     # Print the content
        print(file_content)

def check():
   print("You are overwhelmed by everything that has happened, where are you?"
         " are you okay? well I guess your better check\n")
   choice1 =  input ("Select 1 or 2\n"
                     " 1.Check for injuries\n"
                     " 2.Check bearings\n"
                     )
   if choice1 == "1":
    print("You check yourself for any injuries and by the grace of a great unknown force you are completely fine\n")
   elif choice1 == "2":
      print("eye spy with my little eye something beginning with ummmmmm.... a crashed plane, and a jungle.... nope you have no idea where you are\n")
   else:
      print("input incorrect try again")
      check()

def run_away():
   print(
      "Well I guess you're now feeling a little better about your situation, maybe?"
      " no? oh well any way the strange scent of ash, flesh and the sweet sweet aroma of airplane peanuts fill the air\n"
   )
   choice2 = input("oh look more choices, choose 1 or 2\n"
                   " 1.we all know wild animals love airplane peanuts its a fact or something you could run away\n"
                   " 2.Hey there might be some useful stuff here and the other passengers don't need it anymore search the wreckage\n")
   if choice2 == "1":
      print("Yeah its probably for the best, the corpses where giving me the heebie jeebies\n")
   elif choice2 == "2":
      print("oh look at you! you sweet sweet loot goblin, I am proud of you, that right you take that stuff that the dead won't need anymore\n")
   else:
      print("input incorrect try again")
      run_away()

def next_steps():
   print("All those years of watching survival programmes come back to you\n")

   choices = ["1.water" , "2.food" , "3.shelter"]
   

   while True:
      if len(choices) == 0:
         break
            
      f = "You remember you need to find:\n"

      for item in choices: 
         f += item + "\n"
            
      playerchoice= input(f) 

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


if __name__ == "__main__":
   next_steps()
   