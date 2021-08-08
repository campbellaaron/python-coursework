import math

#Print opening statement
print("Remember logarithmic functions? Great! Let's get started!")
print("Consider the following: \n" +
      "log_b_(x) = e, where b is the base and e is the exponent you use to find x.")
print("In this program, you will be inputing the values of b and x")

#Request user to input the log base and the value of X to determine the exponent
base = int(input("Please enter the number for the log base (b): "))
x = int(input("Please enter the number for the value of x: "))

#Round the exponent answer to 2 decimal places
roundedAnswer = round(math.log(x, base),2)

#Print final result
print("The exponent would be",roundedAnswer)
