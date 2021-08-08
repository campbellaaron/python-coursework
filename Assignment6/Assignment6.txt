#Initialize the array variables for Celsius and Fahrenheit
c_temps = []
f_temps = []

#Initialize variables for warm, hot, and cold day counters
warmDays = 0
hotDays = 0
coldDays = 0

#Display opening message to user 
print("You will be entering the temperatures for the next 10 days in Celsius.")

#Prompt user to enter temperatures until limit has reached
while len(c_temps) < 10 :
    print("Please enter a temperature in Celsius:")
    c = int(input())
    c_temps.append(c)

#Print all ten temperatures to screen
print("The temperatures in Celsius are:\n",c_temps)

#Loop through Celsius temps and convert to Fahrenheit
for c in c_temps:
    f = int((c * 1.8) + 32)
    f_temps.append(f)
    #81 degrees or higher is a hot day
    if f >= 81 :
        hotDays += 1
    #Between 62 and 80 degrees is a warm day
    elif f >= 62 and f <= 80 :
        warmDays += 1
    #Less than 62 would be a cold day
    elif f < 62 :
        coldDays += 1
    
#Print the Fahrenheit temperatures to screen
print("The temperatures in Fahrenheit are:\n",f_temps)

#Display the number of hot, warm, and cold days
print("Based on these temperatures, there will be:\n",hotDays,"hot days\n",warmDays,"warm days\n",coldDays,"cold days.")
