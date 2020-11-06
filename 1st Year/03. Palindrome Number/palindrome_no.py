# Program to check if a given number or string is palindrome or not.
if __name__ == "__main__":

  num = input("Enter a number/string:")
  reverse = num[::-1]
  print("The reversed number/string is:{}".format(reverse))

  if num == reverse:
    print("It is a palindrome")
  else:
    print("It's not a palindrome")