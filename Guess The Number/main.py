import random
from art import logo

def introduction():
  print(logo)
  print("Welcome to the number guessing game!")
  
def difficulty_selection():
  diff = input("Choose your difficulty level: type 'easy' or 'hard': ").lower()
  
  if diff == "easy":
    lives = 10
  elif diff == "hard":
    lives = 5
    
  print(f"You have {lives} lives remaining to the guess the number")
  return lives
  
def choice():
  number = random.randint(1, 100)
  print("I'm thinking of a number between 1 and 100")
  return number
  
def guess(answer, lives_remaining):
  print(answer)
  user_guess = int(input("Make a guess: "))
  
  while user_guess != answer:
    lives_remaining -= 1
    if lives_remaining > 0:
      if user_guess > answer:
        print("lower")
      elif user_guess < answer:
        print("higher")
        
      print(f"You have {lives_remaining} guesses remaining!")
      user_guess = int(input("Make another guess: "))
    else:
      return   
  return user_guess
  
def results(answer, final_guess):
  if answer == final_guess:
    print(f"You guessed it! The number was {answer}. You Win!")
  elif answer != final_guess:
    print(f"You ran out of lives!\nThe number was {answer}. You Lost!")
    
def play_game():
  introduction()
  lives_remaining = difficulty_selection()
  answer = choice()
  final_guess = guess(answer, lives_remaining)
  results(answer, final_guess)

if __name__ == "__main__":
  play_game()
