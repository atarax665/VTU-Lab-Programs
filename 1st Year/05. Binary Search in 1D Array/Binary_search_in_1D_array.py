## To implement binary search technique in 1D Array
from bisect import bisect_left

# Binary search function
def binary_search(lst, key):
  index = bisect_left(lst, key)
  if index != len(lst) and lst[index] == key:
    return index
  else:
    return -1

if __name__ == "__main__":
  lst_input = []
  num = int(input("Enter the number of elements: "))
  print("Enter the Array in ascending order: ")
  
  # Get array list 
  for i in range(0, num):
    item = int(input())
    lst_input.append(item)

  key = int(input("Enter the key to be searched: "))

  result = binary_search(lst_input, key)

  if result != -1:
    print("Key is available at {} location.".format(result + 1))
  else:
    print("Key is not Found.")