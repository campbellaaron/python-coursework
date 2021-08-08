#Print welcome message to screen
print("Welcome to the Dogwood Wood Dog Show! The judges have just issued their \n" +
      "final scores for the wooden dog statues! And they are as follows:")

#Initialize the original five scores to an array
scores = [9.8, 7.6, 9.2, 8.7, 4.0]

#Print scores to user
print(scores)

#Instruct user to replace the 4.0 score with their own
print("Plot twist! It looks like the judge who scored the 4.0 was too busy \n" +
      "eating a Twizzler, so their vote has been voided out. It's your lucky \n" +
      "day! You get to be the guest judge this time.\n")

while (True):
    #Prompt user score
    userScore = float(input("Please enter your score: "))
    #Keep running the prompt until the condition is met
    if (userScore < 0):
        print("Please enter a valid score greater than or equal to 0")
    #Once condition is met, proceed to modifying score array
    else :
        scores.remove(4.0)
        scores.append(userScore)
        for score in scores:
            print("Final scores: ",score)
        break
