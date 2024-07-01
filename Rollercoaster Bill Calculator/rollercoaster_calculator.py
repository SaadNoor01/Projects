print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?\n"))
age = int(input("What is your age?\n"))
bill = 0
if height >= 120:
  print("You can ride this rollercoaster!")
  if age >= 45 and age <= 55:
    print ("free!")
  elif age >= 18:
    print("Adult tickets are $12")
    bill = 12
  elif age >= 12:
    print("youth tickets are $7")
    bill = 7
  else:
    print("Child tickets are $5")
    bill = 5

  photo = input("Do you want a photo taken? y or n.\n")
  if photo == "y":
    bill += 3

else:
  print("Sorry, you have to grow taller before you can ride.")
if photo != "y":
  if photo != "n":
    print("invalid entry")
    exit()
  else:
    print(f"Your bill is ${bill}")
if photo == "y":
  print(f"Your bill is ${bill}")
