#Print opening statement
print("To determine the oldest and youngest of 3 siblings, please enter \n" + 
      "their ages below: ")

firstAge = int(input("First age: "))
secondAge = int(input("Second age: "))
thirdAge = int(input("Third age: "))

#Determine the largest number by checking if each value is greater than the other 2
if (firstAge > secondAge) and (firstAge > thirdAge) :
    oldest = firstAge
elif (secondAge > firstAge) and (secondAge > thirdAge) :
    oldest = secondAge
elif (thirdAge > firstAge) and (thirdAge > secondAge) :
    oldest = thirdAge
else :
    print("Default")

#Determine the smallest number by checking if each value is less than the other 2
if (firstAge < secondAge) and (firstAge < thirdAge) :
    youngest = firstAge
elif (secondAge < firstAge) and (secondAge < thirdAge) :
    youngest = secondAge
elif (thirdAge < firstAge) and (thirdAge < secondAge) :
    youngest = thirdAge
else :
    print ("Default")

#Print the result to the screen
print ("The oldest sibling is",oldest,"years old, and the youngest sibling is",
       youngest,"years old.")

