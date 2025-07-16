import random
from art import logo


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards."""
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
        
	return sum(cards)


def compare(u_score, computer_score):
	if u_score == computer_score:
		return "Draw"
	elif computer_score == 0:
		return "Loose, opponent has Blackjack!"
	elif u_score == 0:
		return "You WIN with a Blackjack!"
	elif u_score > 21:
		return "You went over. You loose."
	elif computer_score > 21:
		return "Computer went over. You WIN."
	elif u_score > computer_score:
		return "You WIN"
	else:
		return "You loose!"
	

def play_game():
	user_cards = []
	computer_cards = []
	user_score = -1
	computer_score = -1
	is_game_over = False

	print(logo)

	for _ in range(2):
		user_cards.append(deal_card())
		computer_cards.append(deal_card())

	while not is_game_over:
		user_score = calculate_score(user_cards)
		computer_score = calculate_score(computer_cards)
		print(f"Your cards: {user_cards}, current score: {user_score}.")
		print(f"Computer's first card: {computer_cards[0]}.")

		if user_score == 0 or computer_score == 0 or user_score > 21:
			is_game_over = True
		else:
			user_should_deal = input("Type 'y' to get another card, or type 'n' to pass: ")
			if user_should_deal == 'y':
				user_cards.append(deal_card())
			else:
				is_game_over = True

	while computer_score != 0 and computer_score < 17:
		computer_cards.append(deal_card())
		computer_score = calculate_score(computer_cards)

	print(f"Computer cards: {computer_cards}, score: {computer_score}.")
	print(compare(user_score, computer_score))


while input("Do you want to play a game of the Blackjack? Type 'y' or 'n': ") == 'y':
	print('\n' * 20)
	play_game()