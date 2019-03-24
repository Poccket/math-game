import sys
if sys.version_info[0] != 3:
	raise Exception("This version must be using Python 3!")

import random
import math

def canBeInt(inp):
	try:
		int(inp)
		return True
	except ValueError:
		return False
		
def getInt(text="Enter number: "):
	a = "NaN"
	while True:
		a = input(text)
		if canBeInt(a):
			return int(a)
		else:
			print("You need to input an integer!")

play = True

while play == True:
	print("\n" * 100)
	
	min = 1
	max = 100
	# min = getInt("Enter minimum number: ")
	max = getInt("Enter maximum number: ")
	
	win = False
	num = random.randint(min,max)
	maxGuess = math.ceil(math.log2(max))
	if maxGuess < 1: maxGuess = 1;

	print("Using min " + str(min) + ", and max " + str(max) + ".")
	print("The computer will now think of a number.")
	print("You must guess the number, and the computer will tell you if it's higher or lower.")
	guessCount = 0
	while True:
		guess = getInt("Enter your guess: ")
		guessCount += 1
		if (guess == num):
			break
		if (guess > num):
			print("Your guess was too high.")
			continue
		if (guess < num):
			print("Your guess was too low.")
			continue
		sys.exit("Something went wrong with the guess functionality!")
	print("You win! The answer was " + str(num) + ", and your guess count was " + str(guessCount) + " out of " + str(maxGuess) + " par guesses")
	replay = None
	while True:
		replay = input("Would you like to play again? (y/n)")
		if (replay == "y"):
			break
		if (replay == "n"):
			print("Exiting...")
			play = False
			break
		print("Please enter a correct input! y or n!")