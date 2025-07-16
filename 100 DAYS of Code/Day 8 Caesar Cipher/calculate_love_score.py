# Calculate Love Score

def calculate_love_score(name1, name2):

	word_true = "true"
	word_love = "love"

	combined_names = name1 + name2
	lower_names = combined_names.lower()

	arr_true = [None] * len(word_true)
	arr_love = [None] * len(word_love)

	# checking word TRUE
	for i in range(len(arr_true)):
		counter = 0
		for char in lower_names:
			if char == word_true[i]:
				counter += 1
		arr_true[i] = counter

	# checking word LOVE
	for i in range(len(arr_love)):
		counter = 0
		for char in lower_names:
			if char == word_love[i]:
				counter += 1
		arr_love[i] = counter

	sum_true = sum(arr_true)
	sum_love = sum(arr_love)
	result = str(sum_true) + str(sum_love)
	print(result)


name1 = input("Name of 1st person: ")
name2 = input("Name of 2nd person: ")

calculate_love_score(name1, name2)

