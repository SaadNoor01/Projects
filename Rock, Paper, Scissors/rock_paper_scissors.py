rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

player = int(input('Lets play Rock, Paper & Scissors. Enter "0" for Rock, "1" for Paper or "2" for Scissors\n'))

if player != "0" and player != "1" and player != "2":
    print("Wrong input, try again!")
else:
    computer = random.randint(0,2)
    
    choice = [rock, paper, scissors]
    
    player_choice = choice[player]
    computer_choice = choice[computer]
    
    print(player_choice)
    print(computer_choice)
    
    if (player_choice == rock and computer_choice == paper) or (player_choice == paper and computer_choice == scissors) or (player_choice == scissors and computer_choice == rock):
        print("You Lose")
    elif (player_choice == rock and computer_choice == scissors) or (player_choice == paper and computer_choice == rock) or (player_choice == scissors and computer_choice == paper):
        print("You Win")
    elif (player_choice == computer_choice):
        print("It's a Draw")

