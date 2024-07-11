import random
from replit import clear
from art import logo
from art import vs
from game_data import data


def introduction():
  print(logo)

intro = introduction()

questions_chosen = []
score = 0
first_option = random.choice(data)
second_option = random.choice(data)

# make sure they are not the same
def loop_game(first_option, second_option):
  
  while first_option == second_option:
    second_option = random.choice(data)
  
  second_option_ind = data.index(second_option)
  questions_chosen.append(second_option_ind)
  
  # get_values function
  first_option_values = list(first_option.values())
  second_option_values = list(second_option.values())
  
  # print statement
  print(f"Compare A: {first_option_values[0]}, {first_option_values[2]}, from {first_option_values[3]}")
  print(vs)
  print(f"Compare B: {second_option_values[0]}, {second_option_values[2]}, from {second_option_values[3]}")
  
  followers = [first_option_values[1], second_option_values[1]]
  
  correct_choice = 0
  for x in followers:
    if x > correct_choice:
      correct_choice = x

  correct_answer = ""
  ind_ans = followers.index(correct_choice)
  if ind_ans == 0:
    correct_answer = "a"
  elif ind_ans == 1:
    correct_answer = "b"

  user_choice = input("Who has more followers: Type 'A' or 'B': ").lower()
  
  if user_choice == correct_answer:
    score = len(questions_chosen)
    clear()
    introduction()
    print(f"You're right! Current Score: {score}.")
    first_option_new = second_option
    second_option_new = random.choice(data)
    loop_game(first_option_new, second_option_new)

  else:
    score = len(questions_chosen) - 1
    clear()
    introduction()
    print(f"Sorry, that's the wrong answer! Final Score: {score}")
  
  
loop_game(first_option, second_option)
