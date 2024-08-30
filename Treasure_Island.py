print("Welcome to Treasure Island!")
print("Your mission is to find the treasure.")
left_or_right = input("You're at a cross road. Where do you want to go? \nType 'left' or 'right': \n")

if left_or_right == "right":
    print("Fall into a hole. Game Over.")
if left_or_right == "left":
    swim_or_wait = input("Do you want to 'swim' or 'wait'? ")
    if swim_or_wait == "wait":
        which_door = input("Which door would you like to go? \n'Red', 'Blue' or 'Yellow': ")
        if which_door == "Red":
            print("Burned by fire. Game Over.")
        elif which_door == "Blue":
            print("Eaten by beasts. Game Over.")
        elif which_door == "Yellow":
            print("You Win!")
        else:
            print("Game Over.")

    else:
        print("Attacked by trout. Game Over.")