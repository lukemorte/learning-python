import random
from art import logo


def show_welcome_screen():
    print(logo)
    print("Welcome to the Number Guessing Game!")


def set_secret_number(num_range):
    rnd = random.randrange(num_range.start, num_range.stop)
    print(f"I'm thinking of a number between {num_range.start} and {num_range.stop}.")
    return rnd


def set_difficulty():
    diff = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if diff == 'easy':
        return 10
    elif diff == 'hard':
        return 5
    

secret_number = None
attempts = None


show_welcome_screen()
secret_number = set_secret_number(range(0, 100))
attempts = set_difficulty()

print(f"You have {attempts} attempts.")



