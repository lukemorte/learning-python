
import random

stages = [
    '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
          |
          |
          |
          |
    =========
    '''
]

word_list = ["aadwark", "baboon", "camel"]

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

	guess = input("Guess a letter: ").lower()

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
		print(stages[lives])

	if "_" not in display:
		game_over = True
		print("You WIN. GAME OVER.")

	if lives == 0:
		game_over = True
		print("YOU DIE. GAME OVER.")
