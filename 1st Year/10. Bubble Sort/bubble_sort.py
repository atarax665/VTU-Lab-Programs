## Program to implement bubble sort

def bubble_sort(arr):
    length = len(arr)
    for i in range(length - 1):
        for j in range(0, length - i - 1):
            if arr[j] > arr[j + 1]:
              ## Swapping the right adjacent number
                t = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = t
    return arr


if __name__ == "__main__":
    input_arr = []
    num = int(input("Enter the number of numbers: "))
    print("Enter the array: ")

    for item in range(0, num):
        input_arr.append(int(input()))

    print("The given array is : {}".format(input_arr))

    print("Array after bubble sorting is: {}".format(bubble_sort(input_arr)))
    exit(0)

'''
Sample output
Enter the number of numbers: 5
Enter the array: 
3
1
6
4
8
The given array is : [3, 1, 6, 4, 8]
Array after bubble sorting is: [1, 3, 4, 6, 8]

'''