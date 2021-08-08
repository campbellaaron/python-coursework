#Initialize list of five students
studentsList = ["Sandra Dee",
                "Johnny Appleseed",
                "James Kirk",
                "Quentin Florentino",
                "Ronald Weasley"]

#Initialize variables for student grades to compute
gradeList = []
studentGradeTotal = 0
studentGradeAvg = 0

#Print opening statement 
print("Please input the grades for the following students")

#Iterate through list of students
for student in studentsList:
    print("Enter the grade for",student)
    #Prompt user to input grade for each student as it loops
    studentGrade = float(input())
    #Add each grade to a new list
    gradeList.append(studentGrade)
    studentGradeTotal += studentGrade

#Take the student grade total and divide by the number of students for the average
studentGradeAvg = round((studentGradeTotal / 5),1)

#Convert average to string and print the result to the screen
print("The average grade for all five students is " +
      str(studentGradeAvg) + "%, and the \n" +
      "highest grade was " + str(max(gradeList)) + "%.")
    
    
