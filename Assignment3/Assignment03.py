#Establish constant values for prices and tiers
budgetQuality = 2.00
standardQuality = 5.50
premiumQuality = 9.50

#Define the function that calculates carpeting costs
def costOfCarpeting (length, width, quality) :
    #Multiply length times width to get square feet
    sqFt = length * width
    #Multiply square feet by selected quality tier to get cost per square foot
    costPerRoom = format(sqFt * quality,'.2f')
    
    #Print the result to the screen
    print("The cost to carpet your room is $" +
          costPerRoom + " at $" + str(format(quality,'.2f')) + " per square foot.")
    return

#Print opening statement
print("Welcome to UMGCarpeting! Where we 'lay the groundwork' for your success!\n")
print("Enter the number of your selection:\n" +
      "1. Budget Quality Carpeting (our cheapest) -- $2.00\n" +
      "2. Standard Quality Carpeting (our most popular) -- $5.50\n" +
      "3. Premium Quality Carpeting (our fanciest, with that special padding) -- $9.50\n")

#Prompt user for input of carpet quality
selectedQuality = int(input("Which would you prefer? "))

#Determine user selection and assign it to a variable
if (selectedQuality == 1) :
    carpetQuality = budgetQuality
elif (selectedQuality == 2) :
    carpetQuality = standardQuality
elif (selectedQuality == 3) :
    carpetQuality = premiumQuality
else :
    print("Sorry, that is not a valid selection. Thank you!")

#Prompt user for measurements of room in ft
print("\nGreat! Now it's time to enter the measurements of your room!")
roomWidth = float(input("Please enter the width of your room, in feet: "))
roomLength = float(input("Please enter the length of your room, in feet: "))

#Call the function to calculate the carpeting cost
costOfCarpeting(roomLength, roomWidth, carpetQuality)
