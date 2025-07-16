
import random

word_list = ["aadwark", "baboon", "camel"]

# TODO-1 - randomly choose a word from the word_list and assign it to a variable called chosen_word.
# TODO-2 - ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
# TODO-3 - check if the letter the user guessed (guess) is one of the letters in the chosen_word. Write "Right" if it is, write "Wrong" if it's not.

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)

for position in range(word_length):
	placeholder += "_"

print(placeholder)

guess = input("Guess a letter: ").lower()

display = ""

for letter in chosen_word:
	if letter == guess:
		display += letter
	else:
		display += "_"

print(display)

