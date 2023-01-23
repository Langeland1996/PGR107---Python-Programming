from math import sqrt

# 1. What are the values of the following expressions? In each line, assume that:
x = 2.5
y = -1.5
m = 18
n = 4

print("Task - 01")
print(x + n * y - (x + n) * y)
print(m // n + m % n)
print(5 * x - n / 5)
print(1 - (1 - (1 - (1 - (1 - n)))))
print(sqrt(sqrt(n)))
print("\n")

# 2. What are the values of the following expressions, assuming that n is 17 and m is 18?
n = 17
m = 18

print("Task - 02")
print(n // 10 + n % 10)
print(n % 2 + m % 2)
print((m + n) // 2)
print((m + n) / 2.0)
print(int(0.5 * (m + n)))
print(int(round(0.5 * (m + n))))
print("\n")

# 3. What are the values of the following expressions? In each line, assume that:
s = "Hello"
t = "World"

print("Task - 03")
print(len(s) + len(t))  # 5 + 5 = 10
print(s[1] + s[2])  # e + l = el
print(s[len(s) // 2])  # s[5 // 2] = s[2] = l
print(s + t)  # HelloWorld
print(t + s)  # WorldHello
print(s * 2)  # HelloHello
print("\n")

# 4. Write a program that prompt the user for two integers and then prints:
# a. The sum
print("Task - 04")


def theSum(arg1, arg2):
    return arg1 + arg2


print(theSum(20, 25))


# b. The difference
def theDifference(arg1, arg2):
    if arg1 > arg2:
        total = arg2 - arg1
        return total
    elif arg1 < arg2:
        total = arg1 - arg2
        return total
    else:
        total = arg1 - arg2
        return total


print(theDifference(20, 25))


# c. The product
def theProduct(arg1, arg2):
    return arg1 * arg2


print(theProduct(20, 25))


# d. The average
def theAverage(arg1, arg2):
    total = arg1 + arg2
    return total / 2


print(theAverage(20, 25))


# e. The distance (absolute value of the difference)
def theDistance(arg1, arg2):
    if arg1 < arg2:
        total = arg2 - arg1
        return total
    elif arg1 > arg2:
        total = arg1 - arg2
        return total
    else:
        total = arg1 - arg2
        return total


print(theDistance(20, 25))


# f. The maximum

def theMaximum(arg1, arg2):
    if arg1 > arg2:
        return arg1
    else:
        return arg2


print(theMaximum(20, 25))


# g. The minimum
def theMinimum(arg1, arg2):
    if arg1 > arg2:
        return arg2
    else:
        return arg1


print(theMinimum(20, 25))
print("\n")

# 5. Properly format the output in Exercise 4 as follows.ss
print("Task - 05")


def formatFunction(arg1, arg2):
    print("-------------------------")
    print("| Enter number 1: %4d %2s" % (arg1, "|"))
    print("| Enter number 2: %4d %2s" % (arg2, "|"))
    print("| Sum = %14d %2s" % (theSum(arg1, arg2), "|"))
    print("| Difference = %7d %2s" % (theDifference(arg1, arg2), "|"))
    print("| Product = %10d %2s" % (theProduct(arg1, arg2), "|"))
    print("| Average = %10d %2s" % (theAverage(arg1, arg2), "|"))
    print("| Distance = %9d %2s" % (theDistance(arg1, arg2), "|"))
    print("| Maximum = %10d %2s" % (theMaximum(arg1, arg2), "|"))
    print("| Minimum = %10d %2s" % (theMinimum(arg1, arg2), "|"))
    print("-------------------------")


formatFunction(20, 25)

# 6. Write  a  program  that  asks  the  user  for  the  lengths  of  the  sides  of  a  rectangle.  Then  print  the
# area  and perimeter of the rectangle.
print("\nTask - 06")


def area_and_perimeter_calculator():
    print("\nWelcome to the area and perimeter calculator program")
    length = int(input("Whats the length of the rectangle?\n"))
    width = int(input("Whats the width of the rectangle?\n"))

    area = length * width
    perimeter = 2 * (length + width)

    print("%10s %10d" % ("Area of the rectangle:", area))
    print("%10s %5d" % ("Perimeter of the rectangle:", perimeter))


# area_and_perimeter_calculator()

# 7. Write  a  program  that  initializes  a  string  variable  and  prints  the  first  two  characters,
# followed  by  three periods, and then the last two characters. For example, if the string is initialized to
# "Mississippi", then print Mi...pi.
print("\nTask - 07")


def first_and_last_two_characters(arg1):
    firstTwoChars = arg1[0] + arg1[1]
    lastTwoChars = arg1[len(arg1) - 2] + arg1[len(arg1) - 1]

    finalString = firstTwoChars + "..." + lastTwoChars
    return finalString


print(first_and_last_two_characters("Mississippi"))


# 8. Write a program that reads a five.digit positive integer and breaks it into a sequence of individual digits.
# For example, the input 16384 is displayed as 1 6 3 8 4

def five_digits_with_space(arg1):

    arg1ToString = str(arg1)
    print(arg1ToString)
    digit1 = arg1ToString[0]
    digit2 = arg1ToString[1]
    digit3 = arg1ToString[2]
    digit4 = arg1ToString[3]
    digit5 = arg1ToString[4]

    digitWithSpace = digit1 + " " + digit2 + " " + digit3 + " " + digit4 + " " + digit5
    return digitWithSpace


print(five_digits_with_space(16384))
