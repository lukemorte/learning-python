# random password generator

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', ']', '^', '_', '{', '|', '}', '~']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

password = ""
print("Welcome to the PyPassword Generator!")

nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

all = [letters, symbols, numbers]
all_counts = [nr_letters, nr_symbols, nr_numbers]

lenpass = nr_letters + nr_symbols + nr_numbers

for i in range(0, lenpass):
	arr = []	
	arr.append(random.choice(letters))
	arr.append(random.choice(symbols))
	arr.append(random.choice(numbers))

	arr_types = []
	if all_counts[0] > 0:
		arr_types.append(0)
	if all_counts[1] > 0:
		arr_types.append(1)
	if all_counts[2] > 0:
		arr_types.append(2)

	choice = random.choice(arr_types)
	all_counts[choice] -= 1
	password += arr[choice]

print(f'Your generated password: {password}')