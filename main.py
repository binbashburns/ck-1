answer = input("Would you like to play a game? (yes/no)")

if answer.lower().strip() == "yes":

    answer = input("You reach a crossroads, would you like to go left of right? (left/right)").lower().strip()

    if answer == "left":
        answer = input("You encounter a monster, would you like to run or attack? (run/attack)")

        if answer == "attack":
            print("This was not a good idea, you lost!")
        else:
            print("Good choice, you made it away safely.")

            answer = input("You see a car and a plane. Which would you like to take? (car/plane)")

            if answer == "plane":
                print("You don't know how to fly a plane! Game Over :[")
            else:
                print("You got away safely! You win!")
    
    elif answer == "right":
        print("You were abducted by aliens! Game Over :[")

else:
    print("That's too bad!")