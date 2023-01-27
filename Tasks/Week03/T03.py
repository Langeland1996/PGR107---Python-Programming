"""
3. Write a program that assigns letter grade for a quiz according
to the following table and then prints the letter grade.

Print a message if the input is not valid.
 _________________
| Score  | Grade |
|----------------|
90 - 100 |   A   |
80 - 89  |   B   |
70 - 79  |   C   |
60 - 69  |   D   |
  > 60   |   F   |
|----------------|

Sample Output
    Enter the score (0-100): 97
    The letter grade is A
 Another Sample Output
    Enter the score (0-100): 44
    The letter grade is F

 Another Sample Output
    Enter the score (0-100): 120
    Invalid input. The score must be in the range (0-100)
"""


def quizGrade(arg):
    if arg > 100:
        print("input is higher then 100.")
    elif arg < 1:
        print("input is lower then 1")
    elif 100 >= arg >= 90:
        print("A")
    elif 89 >= arg >= 80:
        print("B")
    elif 79 >= arg >= 70:
        print("C")
    elif 69 >= arg >= 60:
        print("D")
    else:
        print("F")


print("Task 03\n")

print("\nInput is -1")
quizGrade(-1)

print("\nInput is 101")
quizGrade(101)

print("\nInput is 59")
quizGrade(59)

print("\nInput is 60")
quizGrade(60)

print("\nInput is 77")
quizGrade(77)

print("\nInput is 99")
quizGrade(99)
