"""
2. Write a program that uses an if/elif/else sequence to validate the user’s input to be in the range 1-10. The
number is entered by the user and the program will determine if the number is between 1 and 10. If the
number entered is less than 1, the program will print “The number you entered is < 1”. If the number
entered is greater than 10, the program will print “The number you entered is > 10”. If the number is
between 1 and 10, the program will print the number.

*** Sample Output ***

Enter a number between 1 and 10 --> 12
The number you entered is > 10
Enter a number between 1 and 10 --> -2
The number you entered is < 1
Enter a number between 1 and 10 --> 5
The number you entered is 5

"""


def func(arg):
    if arg > 10:
        print("The number (%d) you entered is > 10." % arg)
    elif arg < 1:
        print("The number (%d) you entered is < 1." % arg)
    else:
        print("The number you entered is (%d)." % arg)


print("Input is 11")
func(11)

print("Input is 7")
func(7)

print("Input is -1")
func(-1)
