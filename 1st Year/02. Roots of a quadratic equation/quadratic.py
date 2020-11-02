## To compute roots of quadratic equation
import math

def equationroots(a, b, c):
  # It's not possible to find roots when a=0 & b=0
  if a == 0 and b == 0:
    print("Roots cannot be determined!")
    return

  # If a is 0, then equation is not quadratic, but Liner
  if a == 0:
    print("Liner Equation:")
    print("Root is: {}".format(- c / b))
    return

  # calculating discriminate using formula
  dis = b * b - 4 * a * c
  sql_val = math.sqrt(abs(dis))

  if dis > 0:
    r1 = (- b + sql_val) / (2 * a)
    r2 = (- b - sql_val) / (2 * a)
    print("Roots are real and distinct:")
    print("Root 1: {} Root 2: {}".format(r1, r2))
  ## root are real
  elif dis == 0:
    r1 = r2 = - b / (2 * a)
    print("The roots are real and equal:")
    print("Root 1: {} Root 2: {}".format(r1, r2))
  # when discriminant is less than 0
  else:
    r = - b / (2 * a)
    print("The roots are imaginary:")
    print("Roo1: {} + i{}".format(r, sql_val))
    print("Roo1: {} - i{}".format(r, sql_val))
  return


if __name__ == "__main__":

  a, b, c = [int(x) for x in input("Enter the coefficients of x:").split()]

  equationroots(a, b, c)