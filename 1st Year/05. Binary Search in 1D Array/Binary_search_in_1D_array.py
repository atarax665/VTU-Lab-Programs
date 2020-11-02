## To implement binary search technique in 1D Array

# It returns location of key in list
# if present, else returns -1
def binary_search(lst, key):
    min = 0
    max = len(lst) - 1
    while min <= max:
        mid = (min + max) // 2
        if lst[mid] == key:
            return mid

        if lst[mid] < key:
            min = mid + 1
        else:
            max = mid - 1
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
        print("Key is available at index {}.".format(result + 1))
    else:
        print("Key is not Found.")

"""

Sample output
Enter the number of elements: 5
Enter the Array in ascending order: 
1
2
4
6
7
[1, 2, 4, 6, 7]
Enter the key to be searched: 4
Key is available at index 3.

Enter the number of elements: 6
Enter the Array in ascending order: 
3
5
6
8
9
13
[3, 5, 6, 8, 9, 13]
Enter the key to be searched: 13
Key is available at index 6.

"""
