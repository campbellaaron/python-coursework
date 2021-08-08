import re

#Print password requirements to screen
print("To continue, you need a strong password.\n The password must be a " +
      "minimum of 8 characters and a maximum of 22, \ncontain at least 1 number, the '#' symbol, and it cannot " +
      "contain the following: \n -- The characters 'umgc' consecutively \n" +
      " -- the # symbol as the first or very last character")

#Determine substring to exclude in password
substring = "UMGC"

while True:
    #Prompt user for a password
    userPassword = str(input("Type in password and press 'Enter' here:  "))
    #If password is greater than or equal to eight characters and less than or equal to 22
    if (len(userPassword) <= 22) and (len(userPassword) >= 8) :
        #If password starts or ends with #, alert user
        if userPassword.startswith("#") or userPassword.endswith("#"):
            print("Password cannot begin or end with '#'")
        #If password does not contain the # symbol in the password, alert user
        elif userPassword.find("#") == -1 :
            print("Password must contain the '#' symbol")
        #If the password contains the substring 'UMGC', alert the user
        elif re.search(substring.lower(), userPassword):
            print("The sequence 'UMGC' cannot appear consecutively")
        elif re.search(substring.upper(), userPassword):
            print("The sequence 'UMGC' cannot appear consecutively")
        elif re.search("uMgC", userPassword):
            print("The sequence 'UMGC' cannot appear consecutively")
        elif re.search("UmGc", userPassword):
            print("The sequence 'UMGC' cannot appear consecutively")
        #If the password does not contain a number, alert the user
        elif not re.search("[0-9]", userPassword):
            print("Password must contain a number")
        else :
            #If the conditions are met, break the loop
            break
    else :
        print("Password cannot be less than 8 characters or exceed 22 characters..")
