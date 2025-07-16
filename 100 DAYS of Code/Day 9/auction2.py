# auction

def find_highest_bidder(bidding_dictionary):
	winner = ""
	highest_bid = 0
	for bidder in bidding_dictionary:
		bid_amount = bidding_dictionary[bidder]
		if bid_amount > highest_bid:
			highest_bid = bid_amount
			winner = bidder
	
	print(f"The winner is {winner} with ${bidding_dictionary[winner]}")


auctionContinue = True
bids = {}

while auctionContinue == True:

	name = input("What is your name?: ")
	price = int(input("What's your bid?: $"))

	bids[name] = price

	shouldContunue = input("Are there any oter bidders? Type 'yes' or 'no': ")
	print('\n' * 100)

	if (shouldContunue == 'no'):
		auctionContinue = False

	find_highest_bidder(bids)

dictionary_people_ages = {'Kate': 7, 'Mike': 12, "Luke": 13, "Michael": 25, "Marcel": 17, "Oliver": 4}
dictionary_people_info = {'name': Kate, 'age': 7, 'gender': 'female', 'born_city': 'Prague', 'salary': 1200, 'hobby': 'skateboard'}

