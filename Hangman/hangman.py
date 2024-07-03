import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#Testing code
print(f'the solution is {chosen_word}.')

display = []
for x in chosen_word:
    display += "_"
print(display)

guess = input("Guess a letter: ").lower()

for letter in chosen_word: # in-progress
    if letter == guess:
        ind1 = chosen_word.index(letter)
        display[ind1] = letter


print(display)
