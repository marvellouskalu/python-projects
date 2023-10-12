print("Welcome to Treasure Island.")
print("Your mission is to find the treasure")
way= input("You are at a cross road. Which way would you love to go? Type left or right\n")
if way == "left":
  move= input("You have come to a lake. There is an island in the middle of the lake.Type 'wait' to wait for a boat or 'swim' to move across the lake\n")
  if move== "wait":
     colour= input("You arrived at a house! The house has three doors. 'red' 'yellow' and 'blue'. Choose one colour\n")
     if colour == "red":
        print("You were burned by fire. Game over!")
     elif colour == "blue":
        print("You were eaten by beasts. Game over!")
     elif colour == "yellow":
            print("You win")
     else:
            print("game over")
  else:
        print("You were attacked by trout. Game over")
else:
    print("Oops! Try again later")





