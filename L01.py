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


# 5. Properly format the output in Exercise 4 as follows.
print("Task - 05")
def formatFunction(arg1, arg2):

    print("-------------------------")
    print("| Enter number 1:", arg1, "   |")
    print("| Enter number 2:", arg2, "   |\n|                       |")
    print("| Sum = ", theSum(arg1, arg2), "            |")
    print("| Difference = ", theDifference(arg1, arg2), "     |")
    print("| Product = ", theProduct(arg1, arg2), "       |")
    print("| Average = ", theAverage(arg1, arg2), "      |")
    print("| Distance = ", theDistance(arg1, arg2), "        |")
    print("| Maximum = ", theMaximum(arg1, arg2), "        |")
    print("| Minimum = ", theMinimum(arg1, arg2), "        |")
    print("-------------------------")


formatFunction(20, 25)
# 6.
