from replit import clear
from art import logo
print(logo)
bid_dic = {}

def find_highest_bidder(bid_dic):
  highest_bid = 0
  highest_bidder = ""
  for key in bid_dic:
    if bid_dic[key] > highest_bid:
      highest_bid = bid_dic[key]
      highest_bidder = key
  print(f"The winner is {highest_bidder} with a bid of ${highest_bid}")
  
bidding_finished = False
while not bidding_finished:
  name = input("What is your name?: ").lower()
  bid = int(input("What is your bid amount?: $"))
  bid_dic[name] = bid
  new_bidder = input('Is there another bidder? type "yes" or "no"\n')
  if new_bidder == "no":
    bidding_finished = True
    find_highest_bidder(bid_dic)
  elif new_bidder == "yes":
    clear()
