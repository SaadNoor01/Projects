PLACEHOLDER = "[name]"

with open("Input/Names/invited_names.txt") as file:
    names = file.readlines()

names = [name.strip() for name in names]

with open("Input/Letters/starting_letter.txt") as letter:
    start_letter = letter.read()

for name in names:
    final_letter = start_letter.replace(PLACEHOLDER, f"{name}")
    with open(f"Output/ReadyToSend/letter_for_{name}.txt", mode="w") as mail:
        mail.write(final_letter)
