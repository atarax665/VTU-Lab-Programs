## To implement functions to check if a number is prime or not

def is_prime(num):

  #Corner cass
  if(num <= 1):
    return False
  if(num <= 3):
    return True

  # num is divisible by 2 or 3
  # skip five numbers and reduce loop
  if(num % 2 == 0 or num % 3 == 0):
    return False

  # only need to check 6k + 1
  i = 5
  while ( i * i <= num):
    if num % i == 0 or num % (i + 2) == 0:
      return False
    i += 6

  return True


if __name__ == "__main__":

  num = int(input("Enter the number: "))
  result = is_prime(num)

  if result:
    print(num, " is a prime.")
  else:
    print(num, "is not a prime.")

'''

Sample output
Enter the Number----> 7
7 is a Prime Number

Enter the Number----> 9
9 is not Prime Number

'''