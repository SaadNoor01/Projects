import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#Testing code
print(f'The solution is {chosen_word}.')

display = []
for x in chosen_word:
    display += "_"
print(display)

guess = input("Guess a letter: ").lower()

ind_num = 0
for letter in chosen_word:
    ind_num += 1
    if letter == guess:
        display[ind_num - 1] = letter

print(display)
