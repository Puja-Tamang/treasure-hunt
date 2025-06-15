print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_  
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____  
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_  
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____  
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the hidden treasure.")

cross_road = input("You're at a crossroad. Where do you want to go? Type 'left' or 'right':\n").lower()
if cross_road == "left":
    ques = input("You come to a lake. Do you want to 'swim' across or 'wait' for a boat?\n").lower()
    if ques == "swim":
        print("You were attacked by a group of wild trout. Game Over.")
    elif ques == "wait":
        door = input("You arrive safely at the island. There is a house with 3 doors: one red, one blue, and one yellow. Which door do you choose?\n").lower()
        if door == "red":
            print("The room is full of fire. Game Over.")
        elif door == "blue":
            print("You are eaten by beasts. Game Over.")
        elif door == "yellow":
            print("You found the treasure! You Win!")
        else:
            print("That door doesn't exist. Game Over.")
    else:
        print("Invalid choice. Game Over.")
else:
    print("You fell into a hidden hole. Game Over.")
