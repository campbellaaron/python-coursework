# Print welcome message
print("Your team won this deathmatch! Would you like to know your kill/death ratio (KDR)? \n")
print("Of course you do!")


while True:
    print("\n") #line break
    # Ask user for kills and deaths
    kills = input("Enter the amount of kills you had: ")
    deaths = input("Enter how many deaths you had: ")

    # Calculate and convert to float
    kills = float(kills)
    deaths = float(deaths)
    ratio = round((kills / deaths),2)

    #Convert to string
    ratioStr = str(ratio)

    # Print result to screen
    print("Great! Your KDR is " + ratioStr + "!\n")

    # Check if ratio was greater than 1.0
    if (ratio < 1.0) :
        print("Ouch, better luck next time!\n\n")
    else :
        print("You're on the way to top of the leaderboard!\n\n")

    #Check if user wishes to input another value or exit program
    response = input("Would you like to enter a new result? y/n:  ")
    if response == "n" :
        break
    elif response == "y" :
        continue
    else :
        print("Syntax error. Shutting down")
        break


