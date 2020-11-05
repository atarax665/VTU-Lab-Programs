## To implement user-defined function for string functions
def slen(str):
    count = 0
    for item in str:
        count += 1
    return count


def scomp(str_first, str_second):
    if slen(str_first) != slen(str_second):
        return False

    for i in range(slen(str_first)):
        if str_first[i] != str_second[i]:
            return False

    return True


def scat(str_first, str_second):
    return str_first + str_second


if __name__ == "__main__":
    str1 = input("Enter String 1: ")
    str2 = input("Enter string 2: ")

    print("Lenght of String 1:", slen(str1))
    print("Length of String 2:", slen(str2))

    if scomp(str1, str2):
        print("The strings {}, {} are equal.".format(str1, str2))
    else:
        print("The strings {}, {} are not equal.".format(str1, str2))

    print("The concatenated string is: {}".format(scat(str1, str2)))

"""
Sample output
Enter String 1: ads
Enter string 2: asdfsdf

Lenght of String 1: 3
Length of String 2: 7
The strings ads, asdfsdf are not equal.
The concatenated string is: adsasdfsdf

"""
