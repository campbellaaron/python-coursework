favChar = "Minnie Mouse"
charGuess = ''
guessList = []
while charGuess.lower() != favChar.lower() :
	charGuess = str(input("Please enter a guess: "))
	guessList.append(charGuess)
print(guessList)
