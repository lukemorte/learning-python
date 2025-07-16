
def life_in_weeks(age):
	years_remaining = 90 - age
	weeks = years_remaining * 52
	print(f"You have {weeks} weeks left.")

age = int(input("How old are you? "))
life_in_weeks(age)
