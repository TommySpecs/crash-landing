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
         " are you okay? well I guess your better check")
   choice1 =  input ("Select 1 or 2\n"
                     " 1.Check for injuries\n"
                     " 2.Check bearings\n"
                     )
   if choice1 == "1":
    print("You check yourself for any injuries and by the grace of a great unknown force you are completely fine")
   elif choice1 == "2":
      print("eye spy with my little eye something beginning with ummmmmm.... a crashed plane, and a jungle.... nope you have no idea where you are")
   else:
      print("input incorrect try again")
      check()

def run_away():
   print(
      "Well I guess you're now feeling a little better about your situation, maybe?"
      " no? oh well any way the strange scent of ash, flesh and the sweet sweet aroma of airplane peanuts fill the air"
   )
   choice2 = input("oh look more choices, choose 1 or 2\n"
                   " 1.we all know wild animals love airplane peanuts its a fact or something you could run away\n"
                   " 2.Hey there might be some useful stuff here and the other passengers don't need it anymore search the wreckage")
   if choice2 == "1":
      print("Yeah its probably for the best, the corpses where giving me the heebie jeebies")
   elif choice2 == "2":
      print("oh look at you! you sweet sweet loot goblin, I am proud of you, that right you take that stuff that the dead won't need anymore")
   else:
      print("input incorrect try again")
      run_away()



'''

survival programmes come back to you
Food
Water
Shelter
'''