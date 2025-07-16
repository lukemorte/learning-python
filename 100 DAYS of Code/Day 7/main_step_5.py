
import random
from hangman_art import logo, stages
from hangman_words import word_list

print(logo)

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)

for position in range(word_length):
	placeholder += "_"

print(placeholder)

game_over = False
correct_letters = []
lives = 6

while not game_over:
	print(f"*************************************** {lives} / 6 LIVES LEFT ***************************************")
	guess = input("Guess a letter: ").lower()
	
  	# you guessed already guessed
	if guess in correct_letters:
		print(f"You already guessed letter {guess.upper()}")	

	display = ""

	for letter in chosen_word:

		#1: you guess right
		if letter == guess:
			display += letter
			if not letter in correct_letters:
				correct_letters.append(letter)

		#2: letter already 
		elif letter in correct_letters:
			display += letter

		#3: not guess
		else:			
			display += "_"				

	print(display)

	if guess not in chosen_word:
		lives -= 1
		print(f"The letter {guess.upper()} is not in the word. You loose life.")
		print(stages[lives])

	if "_" not in display:
		game_over = True
		print("You WIN. GAME OVER.")

	if lives == 0:
		game_over = True
		print("YOU DIE. GAME OVER.")
		print(f"******************** The word you were trying to guess was {chosen_word.upper()} ********************")
