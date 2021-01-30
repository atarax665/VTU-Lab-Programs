## To compute sin x using taylor series approximation
import math

if __name__ == "__main__":
    x = float(input("Enter the value in degrees: "))
    num = int(input("Enter the number of terms in Taylor series expansion: "))

    # Convert to radians
    x = (x * 3.151592) / 180
    term = sum = x

    for i in range(1, 10):
        # Term closest to approximation.
        term = (- term * x * x) / (2 * i * (2 * i + 1))
        sum += term

    print("Calculated =", sum)
    print("Builtin function =", math.sin(x))

'''
sample output

Enter the value in degrees: 90
Enter the number of terms in Taylor series expansion: 2
Calculated = 0.9999875016599555
Builtin function = 0.9999875016599559

'''