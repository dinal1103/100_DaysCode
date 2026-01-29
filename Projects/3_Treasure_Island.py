print("Welcome to Treasure Island.")
print("Your missin is to find the treasure.")
print("Your're at a cross road. Where do you want to go?")
first_step = input('Type "left" or "right" \n').lower()

if first_step == "left":
    print('You\'ve come to a lake. There is an island in the middle of the lake.')
    second_step = input('Type "wait" to wait for a boat. Type "swim" to swim across.\n').lower()
    
    if second_step == "wait":
        print("You arrive at the island unharmed. There is a house with 3 doors.")
        third_step = input('One red, one yellow and one blue. Which colour do you choose?\n').lower()
        
        if third_step == "red":
            print("Burned by fire.\nGame Over.")
        elif third_step == "yellow":
            print("You Win!")
        elif third_step == "blue":
            print("Eaten by beast.\nGame Over.")
        else:
            print("Game Over.")
            
    else:
        print("Attacked by trout.\nGame Over.")
    
else:
    print("Fall into a hole.\n Game Over.")
