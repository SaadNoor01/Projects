import random
from art import logo, vs
from game_data import data
from replit import clear


def format_info(option_values):
  """Takes a list and formats the information and 
  returns a string with relevlant info for the user"""
  name = option_values[0]
  description = option_values[2]
  country = option_values[3]
  return f"{name}, {description}, from {country}"


def check_answer(first_option_followers, second_option_followers, user_choice):
  """Checks whether the users selection is correct and returns 
    True or False value"""
  if first_option_followers > second_option_followers:
    return user_choice == "a"
  else:
    return user_choice == "b"


def play_game():
  print(logo)
  score = 0
  second_option = random.choice(data)
  play = True
  
  while play:
    first_option = second_option
    second_option = random.choice(data)
    
    while first_option == second_option:
      second_option = random.choice(data)
    
    first_option_values = list(first_option.values())
    second_option_values = list(second_option.values())
    
    print(f"Compare A: {format_info(first_option_values)}")
    print(vs)
    print(f"Compare B: {format_info(second_option_values)}")
    
    first_option_followers = first_option["follower_count"]
    second_option_followers = second_option["follower_count"]
    
    user_choice = input("Who has more followers: Type 'A' or 'B': ").lower()
    correct = check_answer(first_option_followers, second_option_followers, user_choice)
    
    clear()
    print(logo)

    if correct:
      score += 1
      print(f"You're right! Current Score: {score}.")
    else:
      print(f"Sorry, that's the wrong answer! Final Score: {score}")
      play = False

if __name__ == "__main__":
  play_game()
