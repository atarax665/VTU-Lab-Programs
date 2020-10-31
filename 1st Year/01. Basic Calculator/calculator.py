import operator
## To implement a calculator

my_operators = {
    '+': [operator.add, "Sum"],
    '-': [operator.sub, "Difference"],
    '*': [operator.mul, "Product"],
    '/': [operator.truediv, "Quotient"],
    '%': [operator.mod, "Remainder"]
}

def calculator(symbol,num1,num2):

  # Find invalid operator
  if symbol not in my_operators:
    print("Invalid operator!!\n")
    return
  # Test condition cannot divide by zero
  if int(num2) == 0 and (symbol in ["/", "%"]):
    print("Cannot divide by zero!!\n")
    return
  result = my_operators.get(symbol)[0](int(num1), int(num2))
  print("{0} = {1}".format(my_operators.get(symbol)[1], result))


if __name__ == "__main__":
  print("Menu:")
  print("Addition\n- Subtraction\n* Multiplication\n/ Division\n% Remainder\n")
  symbol = input("Enter the symbol for operation:")
  print(symbol)
  num1 = input("Enter the first number: ")
  num2 = input("Enter the second number: ")
  print(num1, num2)

  calculator(symbol, num1, num2)