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

password = ""

for char in range(0, nr_letters):
	password += random.choice(letters)

for char in range(0, nr_symbols):
	password += random.choice(symbols)

for char in range(0, nr_numbers):
	password += random.choice(numbers)

password_arr = list(password)
random.shuffle(password_arr)

password = ""
for char in password_arr:
	password += char

print("shuffled password: " + password)




