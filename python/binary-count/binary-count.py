import random
import sys
import math
play = True

while play == True:
	print("\n" * 100)
	min = 1
	max = 100
	# min = int(input("Enter minimum number: "))
	max = int(input("Enter maximum number: "))
	win = False
	num = random.randint(min,max)
	maxGuess = math.ceil(math.log2(max))
	if maxGuess < 1: maxGuess = 1;

	print("Using min " + str(min) + ", and max " + str(max) + ".")
	print("The computer will now think of a number.")
	print("You must guess the number, and the computer will tell you if it's higher or lower.")
	guessCount = 0
	while True:
		guess = int(input("Enter your guess: "))
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