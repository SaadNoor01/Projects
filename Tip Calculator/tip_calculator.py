print("Welcome to the tip calculator!")

bill_str = input("What was the total bill?\n$")
tip_str = input("How much percentage tip would you like to give? 10, 12 or 15\n")
people_str = input("How many people to split the bill?\n")

bill = float(bill_str)
tip = float(tip_str)
people = float(people_str)

total = (bill + (bill * (tip / 100)))
per_person = total / people
result = round(per_person, 2)
result = "{:.2f}".format(result)

print(f"Each person should pay: ${result}")
