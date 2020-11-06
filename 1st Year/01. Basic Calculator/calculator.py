## To implement a calculator


def Sum(num1, num2):
    return "Sum = {}".format(num1 + num2)


def Difference(num1, num2):
    return "Difference = {}".format(num1 - num2)


def Product(num1, num2):
    return "Product = {}".format(num1 * num2)


def Quotient(num1, num2):
    return "Quotient = {}".format(num1 / num2)


def Remainder(num1, num2):
    return "Remainder = {}".format(num1 % num2)


my_operators = {"+": Sum, "-": Difference, "*": Product, "/": Quotient, "%": Remainder}


def calculator(symbol, num1, num2):

    # Find invalid operator
    if symbol not in my_operators:
        print("Invalid operator!!\n")
        return
    # Test condition cannot divide by zero
    if int(num2) == 0 and (symbol in ["/", "%"]):
        print("Cannot divide by zero!!\n")
        return

    print(my_operators.get(symbol)(int(num1), int(num2)))
    return

if __name__ == "__main__":
    print("Menu:")
    print("+ Addition\n- Subtraction\n* Multiplication\n/ Division\n% Remainder\n")
    symbol = input("Enter the symbol for operation:")
    print(symbol)
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    print(num1, num2)

    ## Test for each case +, -, *, /, %
    calculator(symbol, num1, num2)


"""
Enter the symbol for operation:\
\
Enter the first number: 3
Enter the second number: 4
3 4
Invalid operator!!

Sample output
Enter the symbol for operation: ----> +  
Enter the first number: ---->3
Enter the second number:---->4
3 4
Sum = 7

Enter the symbol for operation: ----> -  
Enter the first number: ---->5
Enter the second number:---->4
5 4
Difference = 1

Enter the symbol for operation:*
*
Enter the first number: 4
Enter the second number: 5
4 5
Product = 20

Enter the symbol for operation:/
/
Enter the first number: 7
Enter the second number: 5
7 5
Quotient = 1.4

Enter the symbol for operation:%
%
Enter the first number: 20
Enter the second number: 3
20 3
Remainder = 2

Enter the symbol for operation:/
/
Enter the first number: 3
Enter the second number: 0
3 0
Cannot divide by zero!!
"""
