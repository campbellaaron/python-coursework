#Print opening statement to welcome user
print("Welcome to the Teddy Bear Generator!\n" + 
      "How many teddy bears would you like to produce?\n")

#Prompt user for input of how many bears
bearsToProduce = int(input("Enter the amount of teddy bears and then press 'Enter': "))
#Initialize the amount of bears already produced
bearsProducedSuccessfully = 0

#Produce teddy bears until they reach the amount speficied by user 
while bearsProducedSuccessfully < bearsToProduce :
    bearsProducedSuccessfully += 1
    print("Teddy Bear created successfully...")

#Print total amount of bears produced
print("The total amount of bears produced was",bearsProducedSuccessfully)

