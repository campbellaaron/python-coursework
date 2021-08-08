#Establish constant values for age group prices
childAgeCutoff = 10
seniorAgeCutoff = 65

#Establish constant values for regular, 3D, and discounted movie ticket price
ticketPrice = 9.50
ticketPriceReduction = 4.00
ticket3dSurcharge = 3.50

#Initialize 3D boolean 
movieIs3d = False

#Print opening statement
print("Welcome to Python Cinema!")

#Ask user if they are viewing a 3D movie or regular as input
response3d = input("Are you viewing this movie in 3D? y/n ")

#If user input is 'y' or 'Y' set 3D boolean to True, else keep it false
if (response3d == "y" or response3d == "Y") :
    movieIs3d = True
elif (response3d == "n" or response3d == "N") :
    movieIs3d = False
else :
    print("Invalid entry")

#Ask user for their age as input
patronAge = int(input("What is your age? "))

if patronAge <= 0 :
    print("Sorry, that is not a valid age")
else :
    #Check if user is in the discount age group(s)
    if patronAge >= 65 or patronAge <= 10 :
        #If in the discount age group(s), check if movie is 3D
        if (movieIs3d == True) :
            ticketPrice = format((ticketPrice - ticketPriceReduction) + ticket3dSurcharge,',.2f')
        #If not a 3D movie, just calculate discounted ticket price
        else :
            ticketPrice = format((ticketPrice - ticketPriceReduction),',.2f')
    else :
        if (movieIs3d == True) :
            ticketPrice = format(ticketPrice + ticket3dSurcharge,',.2f')
        else :
            ticketPrice = format(ticketPrice, ',.2f')

    #Convert ticketPrice to string for printing
    ticketPrice = str(ticketPrice)

    #Print final ticket price based on conditions above
    print("Thank you! The ticket price will be $" + ticketPrice + "! Enjoy your movie!")

