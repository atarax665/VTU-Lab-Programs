def bubble_sort(list):
    for i in range(len(list)):
        for j in range(len(list) - 1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]

list = [19, 13, 6, 2, 18, 8]
bubble_sort(list)
print(list)