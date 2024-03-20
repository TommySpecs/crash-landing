def shelter ():
    print("Well you need a place to sleep and protect you from the element maybe a nice comfy shelter would do the trick")
    choice_shelter1 = input("While wandering through the jungle you start finding a good collection of sticks and large leaves, hey look there are a few in a pile here\n 1.add it to your collection\n 2.check it\n")
    if choice_shelter1 == "1":
        print("well done champ your pile of sticks just grew but hey one of those sticks isn't a stick ....there is a venomous snake in the bundle that bites you you die game over")
    elif choice_shelter1 == "2":
        print("using your keen senses and glorious eyesight the sticks you're going to add to your collection look sturdy and perfect for you need\n congratulations you use your gathered materials and make a shelter")
    else:
      print("input incorrect try again")
      shelter ()

      '''
      Need to add movement to food or Water
      need to sort Game over
      '''
