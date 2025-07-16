# auction

bidders = []
auctionContinue = True

while auctionContinue == True:

	aName = input("What is your name?: ")
	aBid = int(input("What's your bid?: $"))

	bidders.append({'aName': aName, 'aBid': aBid})

	shouldContunue = input("Are there any oter bidders? Type 'yes' or 'no': ")
	print('\n' * 100)

	if (shouldContunue == 'no'):
		auctionContinue = False

highest = 0
highestBidder = None

print("all bidders: \n\n")

for bidder in bidders:
	print(f"{bidder['aName']}: ${bidder['aBid']}")
	if bidder['aBid'] > highest:
		highest = bidder['aBid']
		highestBidder = bidder		

print(f"... and the winner is: {highestBidder['aName']} with ${highestBidder['aBid']}")