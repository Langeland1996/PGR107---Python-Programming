# 2. Write programs using for loop that read a line of input as a string and print.
# A. Only the uppercase letters in the string.
def printUppercase(arg):
    correctString = " "
    for i in arg:
        if i.isupper():
            correctString += i
    print(correctString)


print("2a.")
printUppercase("test input")
print("....")
printUppercase("TEST INPUT")
print("....")
printUppercase("TeSt InPuT")
print("\n")


# B. Every second letter of the string.
def printEverySecondLetter(arg):
    count = 0
    correctString = ""
    for i in arg:
        count += 1
        if count % 2 == 0:
            correctString += i
    print(correctString)


print("2b.")
printEverySecondLetter("aTahaias  aias  atahae  acaoararaeacat  asataraianag")  # Expected result - "This is the correct string"
print("....")
printEverySecondLetter("T ")  # Expected result - " "
print("....")
printEverySecondLetter(" T E S T ")  # Expected result - "TEST"
print("\n")

# C. The string, with all vowels replaced by an underscore.
def replaceVowelsWithUnderscore(arg):
    correctString = ""
    for i in arg:
        if i.upper() == "A" \
                or i.upper() == "E" \
                or i.upper() == "I" \
                or i.upper() == "Y" \
                or i.upper() == "O" \
                or i.upper() == "U":
            correctString += "_"
        else:
            correctString += i
    print(correctString)


print("2c.")
replaceVowelsWithUnderscore("A String with vowels yeah?")
print("\n")


# D. The number of digits in the string.
def numberOfDigitsInString(arg):
    count = 0
    for i in arg:
        if i.isdigit():
            count += 1

    print("Number of digits in %d" % count)


print("2d.")
numberOfDigitsInString("String with 3 digits 23")
print("\n")

# E. The number of vowels in the string
def numberOfVowelsInString(arg):
    count = 0
    for i in arg:
        if i.upper() == "A" \
                or i.upper() == "E" \
                or i.upper() == "I" \
                or i.upper() == "Y" \
                or i.upper() == "O" \
                or i.upper() == "U":
            count += 1
    print("Number of vowels in string: %d" % count)


print("2e.")
numberOfVowelsInString("A String with vowels yeah?")
print("\n")




