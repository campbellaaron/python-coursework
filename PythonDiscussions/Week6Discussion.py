#Display opening statement to user
print("To test if a word is a palindrome, please choose a word to analyze:")

#Prompt user for their word choice
userWord = str(input())

#Define a function to reverse the string
def reverseString(text):
    return text[::-1]

#Call the reverse string function
newString = reverseString(userWord)

#Check to see if the string is a palindrome, and long enough to be a palindrome
if (newString.lower() == userWord.lower()) :
    print("The word",userWord,"is a palindrome")
elif len(userWord) < 3 :
    print("Word needs to be minimum of 3 characters")
else :
    print("The word",userWord,"is NOT a palindrome.")
