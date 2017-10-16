#!/usr/bin/python3

import sys

# Function to check if the user wants to quit.
def checkInputText(text):
	if (text in ["q", "quit"]):
		print("Goodbye!")
		exit(0)

# Program starts here.
if __name__ == '__main__':
	print("")
	print("======================")
	print("===== Calculator =====")
	print("======================")
	print("")
	print("- Input 'q' to quit.")
	print("- Made by bart.")
	print("")

	inputText = input("Input a number: ")
	checkInputText(inputText)
	number = float(inputText)

	while (True):
		inputText = input("Do u want to add, subtract, multiply or divide? ")
		checkInputText(inputText)
		operation = inputText

		inputText = input("Insert the number to " + operation + " ")
		checkInputText(inputText)
		number2 = float(inputText)

		if operation == 'add':
			number = number + number2
		if operation == 'subtract':
			number = number - number2
		if operation == 'multiply':
			number = number * number2
		if operation == 'divide':
			number = number / number2

		print("result: " + str(number))
