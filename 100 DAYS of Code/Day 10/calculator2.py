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



# code

operations = {
	'+': add,
	'-': subtract,
	'*': multiply,
	'/': divide,
}

print(calc_art)

programContinue = True

while programContinue == True:

	operationContinue = True
	n1 = float(input("What's the first number?: "))

	while operationContinue == True:

		operation_symbol = getOperationSymbol(operations)
		n2 = float(input("What's the next number?: "))

		result = operations[operation_symbol](n1, n2)
		print(f"{n1} {operation_symbol} {n2} = {result}")

		isOperationContinue = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation ('q' for quit): ")

		if isOperationContinue == 'y':
			n1 = result

		elif isOperationContinue == 'n':
			operationContinue = False

		else:
			operationContinue = False
			programContinue = False
			print("The END. Thank you for using calculator.")





