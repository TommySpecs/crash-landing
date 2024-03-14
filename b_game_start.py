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
   print("You are overwhelmed by everything that has happened, where are you? are you okay? well I gues your better check")
   choice1 =  input ("Select 1 or 2\n 1.Check for injuries\n 2.Check bearings\n")
   if choice1 == "1":
    print("You check yourself for any injuries and by the grace of a great unknown force you are completley fine")
   elif choice1 == "2":
      print("eye spy with my little eye something beginning with ummmmmm.... a crashed plane, and a jungle.... nope you have no idea where you are")
   else:
      print("input incorrect try again")
      check()


if __name__ == "__main__":
   check()

'''
run away?
search wreckage - finding items (inventory)

survival programmes come back to you
Food
Water
Shelter
'''