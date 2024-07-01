print("The Love Calculator is calculating your score...")
name1 = input("What is your name?") 
name2 = input("What is their name?")

name1 = name1.lower()
name2 = name2.lower()
name = name1 + name2
t = name.count ("t")
r = name.count ("r")
u = name.count ("u")
e = name.count ("e")
first_digit = t + r + u + e

l = name.count ("l")
o = name.count ("o")
v = name.count ("v")
e = name.count ("e")
sec_digit = l + o + v + e

first_digit = str(first_digit)
sec_digit = str(sec_digit)

score = int(first_digit + sec_digit)

if score < 10 or score > 90:
  print(f"Your score is {score}, you go together like coke and mentos.")
elif score > 40 and score < 50:
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")
