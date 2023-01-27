"""
Write a program that calculates multiplication, division, addition or subtraction of two numbers, a and b,
entered by the user. The user will also enter operator type (*, /, + or -). If the operator is (*), the program
will compute (a*b). If the operator is (/), the program will compute (a/b) (if b is not equal to zero). If the
operator is (+), the program will compute (a+b). And if the operator is (-), the program will compute a-b.
For any other operators, the program prints the message: “Invalid operator or operator is not in the
list”.

Sample Output
Enter a: 5
Enter b: 4
Enter operator type: *
 Result is 20
"""


def calc(iNumber1, iNumber2, sOperator):
    if sOperator.__eq__("*") | sOperator.__eq__("/") | sOperator.__eq__("+") | sOperator.__eq__("-"):

        if sOperator == "*":
            total = iNumber1 * iNumber2
            print(total)
        elif sOperator == "/":
            if iNumber2 != 0:
                total = iNumber1 / iNumber2
                print(total)
            else:
                print("Secondary number is 0, that's not allowed")
        elif sOperator == "+":
            total = iNumber1 + iNumber2
            print(total)
        elif sOperator == "-":
            total = iNumber1 - iNumber2
            print(total)


    else:
        print("Operator is not valid input, must be +, -, /, or *")


calc(1, 1, "/")
