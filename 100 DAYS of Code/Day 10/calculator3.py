# calculator

from calc_art import calc_art

def add(n1, n2):
	return n1 + n2

def subtract(n1, n2):
	return n1 - n2

def multiply(n1, n2):
	return n1 * n2

def divide(n1, n2):
	return n1 / n2

def getOperationSymbol(operations):
	for symbol in operations:
		print(symbol)
	operation_symbol = input("Pick an operation: ")
	return operation_symbol

def calculator():
	"""
	Calculate the simple mathematical operation
	"""
	print(calc_art)
	shouldAccumulate = True
	n1 = float(input("What's the first number?: "))

	while shouldAccumulate == True:

		operation_symbol = getOperationSymbol(operations)
		n2 = float(input("What's the next number?: "))

		result = operations[operation_symbol](n1, n2)
		print(f"{n1} {operation_symbol} {n2} = {result}")

		isOperationContinue = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")

		if isOperationContinue == 'y':
			n1 = result

		elif isOperationContinue == 'n':
			shouldAccumulate = False
			print('\n' * 20)
			calculator()

		else:
			print('\n' * 20)
			print("The End. Thank you for using The Calculator.")
			return



# code

operations = {
	'+': add,
	'-': subtract,
	'*': multiply,
	'/': divide,
}

calculator()


		





