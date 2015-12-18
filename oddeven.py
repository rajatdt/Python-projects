import random

def oddEven():

	userScore = 0
	compScore = 0

	userChoice = raw_input("what choice would you like to have? odd or even?")
	choice1 = "odd"
	choice2 = "even"
	if (userChoice == choice1 or userChoice == choice2):

		userInput = raw_input("Show your finger(s) user.....")
		print("you chose :")
		print(userInput)

		compInput = random.randrange(1, 10)
		print("The computer chose :")
		print(compInput)

		total = int(userInput)+int(compInput)

		if (userChoice == "even" and total % 2 == 0):
			print("you won, computer lost")
			userScore += 1
		elif (userChoice == "odd" and total % 2 != 0):
			print("you won, computer lost")
			userScore += 1
		else:
			print("Sorry you lost and the computer won")
			compScore += 1


		print("Do you want to play another round ? ")
		playMore = raw_input("Enter y if Yes or n if No")

		if (playMore == "y"):
			oddEven()
		elif (playMore == "n"):
			print("Thanks for playing !!!")
		else: 
			print("Please enter a valid response")

		

	else:

		print("This is an invalid choice")
		oddEven()



	print("Your score is :")
	print(userScore)

	print("computer's score is :")
	print(compScore)
    


oddEven() 