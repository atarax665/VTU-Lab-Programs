# To implement an electricity bill

if __name__ == "__main__":

  name = input("Enter the name:")

  # units should be number
  while True:
    try:
      units = float(input("Enter the no.of.units consumed: "))
      break
    except ValueError:
      print("That's not validate number.")

  # Calculate charge
  if units <= 200:
    charge = units * 0.8
  elif units <= 300:
    '''
      From previous if(), we have determined that units>200,
			but we should charge only 80p for first 200 units, so 200*0.8 = 160
			and the next hundred units to be charged 90p,
			so no.of units to be charged 90p = units - 300
			'''
    charge = 160 + (units - 200) * 0.9
  else:
    '''
			From previous if(), we have determined that units>300, 
			but we should charge only 80p for first 200 units and 90p for next 100, so 200*0.8 + 100*0.9= 250
			and the next units to be charged Rs.1, 
			so no.of units to be charged Rs.1 = units - 300
      '''
    charge = 250 + (units - 300) * 1

  # Additional meter charge
  charge += 100

  # Additional 15% tax
  if charge > 400:
    charge += charge * 0.15

  # Required Output
  print("Name:", name)
  print("Units consumed: ", units)
  print("Charge = Rs ", charge)