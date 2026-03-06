# Calculating Grades (ok, let me think about this one)

# Write a program that will average 3 numeric exam grades, return an average test score, a corresponding letter grade, and a message stating whether the student is passing.

# Average	Grade
# 90+	A
# 80-89	B
# 70-79	C
# 60-69	D
# 0-59	F

# Exams: 89, 90, 90
# Average: 90
# Grade: A
# Student is passing.

# Exams: 50, 51, 0
# Average: 33
# Grade: F
# Student iis failing.

exam_one = int(input("Input exam grade one: "))

exam_two = int(input("Input exam grade two: "))

exam_three = int(input("Input exam grade three: ")) # Error: Use consistent naming patterns...
# Cast it to integer, not string

grades = [exam_one, exam_two, exam_three] # Added commas to seperate each grade

sum = 0
for grade in grades: # Made grade -> grades -- naming convention
  sum = sum + grade

avg = sum / len(grades) # Typo

if avg >= 90: # Condition states 90 + (problem with the question - as per requirements 90 is not accounted for...)
    letter_grade = "A"
elif avg >= 80 and avg <= 89: # Added colon to mark the end of the elif statement
    letter_grade = "B"
elif avg >= 70 and avg <= 79: # Fixed condition to make it easier to understand, and suit requirements
    letter_grade = "C" # Error: Use consitent syntax "" vs "' -> will also cause a syntax error
elif avg >= 60 and avg <= 69:
    letter_grade = "D"
else: # No condition so else:
    letter_grade = "F"

# Removed the unnessecary for loop
print("Exams: " + str(grades[0]) + ", " + str(grades[1]) + ", " + str(grades[2])) # Each exam mark is now printed...
print("Average: " + str(avg))
print("Grade: " + letter_grade)

if letter_grade == "F": # Typo - and comparison operator added...
    print ("Student is failing.") # Missing brackets
else:
    print ("Student is passing.")
