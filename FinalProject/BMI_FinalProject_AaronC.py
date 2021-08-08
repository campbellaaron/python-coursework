#Initialize list of names
individuals = ["JayJay","Andre","Chantel","Eugene","Ysenia","Clawdeen"]

#Initialize array lists for bmi and number of people in each category
bmiList = []
underweightBMI = 0
normalWeightBMI = 0
overweightBMI = 0

#Define function to determine body mass index
def bodyMassIndex(height, weight):
    bmi = (weight * 703) / height**2
    return bmi

#Define function with BMI as parameter to determine if underweight, normal, or overweight
def weightCategory(userBMI):
    #if BMI under 20.5
    if userBMI < 20.5 :
        category = "underweight"
    #else if BMI between 20.5 and 25.0
    elif userBMI >= 20.5 and userBMI < 25.0:
        category = "normal weight"
    #else if BMI greater than or equal to 25.0
    elif userBMI >= 25.0:
        category = "overweight"
    return category

#Prompt user to input BMI in inches and pounds for each individual
for individual in individuals:
    print("Please enter the height in inches and weight in pounds for",individual)
    personHeight = float(input("Height: "))
    personWeight = float(input("Weight: "))
    bmi = round(bodyMassIndex(personHeight, personWeight),2)
    #If BMI is within a certain range, add it to the number of individuals in that category
    if bmi < 20.5:
        underweightBMI += 1
    elif bmi >= 20.5 and bmi < 25.0:
        normalWeightBMI += 1
    elif bmi >= 25.0:
        overweightBMI += 1
    #Add the individuals BMI to a separate list and print to screen
    bmiList.append(bmi)
    print("The BMI of",individual,"is",bmi)

#Loop through the list of BMI and call function if overweight or underweight or normal
for bodymass in bmiList:
    print("A BMI of",bodymass,"is considered to be",weightCategory(bodymass))

#Print the number of individuals for each category to the screen
print("\n")
print("Number of individuals that are underweight:",underweightBMI)
print("Number of individuals that are in the normal range:",normalWeightBMI)
print("Number of individuals that are overweight:",overweightBMI)
