import random
from art import logo


EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def show_welcome_screen():
    print(logo)
    print("Welcome to the Number Guessing Game!")


def set_secret_number(num_range):    
    rnd = random.randint(num_range.start, num_range.stop)
    print(f"I'm thinking of a number between {num_range.start}"
          f"and {num_range.stop}.")
    return rnd


def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == 'easy':
        return EASY_LEVEL_TURNS
    elif level == 'hard':
        return HARD_LEVEL_TURNS


def game_loop(attempts, secret_number):

    game_over = False

    while attempts > 0 and game_over is False:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))

        if guess > secret_number:
            print("Too hight.")
        elif guess < secret_number:
            print("Too low.")
        else:
            game_over = True
        attempts -= 1

    if attempts > 0:
        return True
    else:
        return False


def game():
    secret_number = None
    attempts = None

    show_welcome_screen()
    secret_number = set_secret_number(range(0, 100))
    attempts = set_difficulty()

    win = game_loop(attempts, secret_number)

    if win:
        print(f"You got it! The answer was {secret_number}.")
    else:
        print("You've run out of guesses. GAME OVER.")


# program code

game()
