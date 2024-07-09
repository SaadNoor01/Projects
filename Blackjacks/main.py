from replit import clear
import random
from art import logo

def deal_card():
  """Returns a random card from the deck"""
  deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(deck)
  return card
  
def check_ace(hand, sum):
  """
  Checks if ace in hand results in the sum exceeding 21
  in which case it replace the 11 value for the ace with a 1

  Parameters:
  hand (list): A list of cards held by the players
  sum (int): Total value of the cards in hand for a given player
  
  """
  if hand[-1] == 11 and sum > 21:
    hand[-1] = 1

def play(player_hand, dealer_hand):
  """
  Deals the user a card until user decides to either 
  stop or exceeds a value of 21 for cards in hand

  Parameters:
  player_hand (list): A list of cards held by the User
  dealer_hand (list): A list of cards held by the Computer

  """
  player_hand.append(deal_card())
  check_ace(player_hand, sum(player_hand))
  player_sum = sum(player_hand)

  if player_sum <= 21:
    print(f"Your cards: {player_hand}, current total: {player_sum}")
    print(f"Dealers first card: {dealer_hand[0]}")
    draw = input("type 'y' to get another card, type 'n' to pass: ")
    if draw == "y":
      play(player_hand, dealer_hand)
    else:
      return
  else:
    print(f"Your cards: {player_hand}, current total: {player_sum}")
    print("your hand went above 21, it's a bust!")

def compare(dealer_sum, player_sum):
  """
  Compares the User total against the Computer/Dealers total to determine the outcome of the game

  Parameters:
  dealer_sum (int): The total value of the dealer's cards in hand.
  player_sum (int): The total value of the users cards in hand.

  """
  if dealer_sum <= 21:
    if dealer_sum > player_sum:
      return "You Lose!"
    elif dealer_sum == player_sum:
      return "It's a Draw..."
    elif dealer_sum < player_sum:
      return "You Win!"
  else:
    return "The dealer's hand went over 21, you win!"

def play_game():
  """
  Encompasses the core logic of the BlackJack game.

  """
  print(logo)
  
  # assign two cards to each player
  player_hand = [deal_card(), deal_card()]
  dealer_hand = [deal_card(), deal_card()]
  
  # add value of the current hands
  player_sum = sum(player_hand)
  dealer_sum = sum(dealer_hand)
  
  # print starting condition
  print(f"Your cards: {player_hand}, current total: {player_sum}")
  print(f"Dealers first card: {dealer_hand[0]}")
  
  # decision to continue
  draw = input("type 'y' to get another card, type 'n' to pass: ")
  
  # Call the function for player logic
  if draw == "y":
    play(player_hand, dealer_hand)
  player_sum = sum(player_hand)
  
  # Dealer card drawing logic
  if player_sum <= 21:
  
    while dealer_sum < 17:
      dealer_hand.append(deal_card())
      check_ace(dealer_hand, sum(dealer_hand))
      dealer_sum = sum(dealer_hand)
  
    results = compare(dealer_sum, player_sum)
  
    print(f"Your final hand: {player_hand}, your final total: {player_sum}")
    print(f"Dealer final hand: {dealer_hand}, dealer's final total: {dealer_sum}")
    print(results)


def main():
  play_game()
  while input("Do you want to play another game of BlackJack? Type 'y' or 'n': ") == "y":
    clear()
    play_game()

if __name__ == "__main__":
  main()
