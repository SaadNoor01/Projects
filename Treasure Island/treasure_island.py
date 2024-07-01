print('''
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
 _________|___________| ;`-.o`"=._; ." ` '`." . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
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
print("Your mission is to find the treasure.") 

choice1 = input('You are at a cross road. Which way would you like to go? ... \n          Type "left" or "right"\n')
choice1 = choice1.lower()
choice2 = None
choice3 = None

if choice1 == "left":
          choice2 = input('\nyou arrive at a river.... Now what will you do?\n\nType "wait" to wait and search for a boat or "swim" to swim across\n')
          choice2 = choice2.lower()
          
else:
          print("Yeah right! Game Over")
          exit()

if choice2 == "swim":
          choice3 = input('\nYou swam across the river and see a house with 3 doors...\n\nOne red, one yellow and one blue. Which one do you choose?\n')
          choice3 = choice3.lower()
else:
          print("Back to the Lobby! Game Over")
          exit()

if choice3 == "blue":
          print("Congratulations, You Win!")

else:
          print("Woops, you got caught by the trap door! Game Over!")
          exit()
