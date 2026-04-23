try:
    # taking input
    x = int(input("Enter a number: "))

    # list operation
    numbers = [10, 20, 30]
    print(numbers[x])

    # string operation (can cause type error if changed later)
    print("Result: " + x)

except ValueError:
    print("Error: You entered a non-number value")

except IndexError:
    print("Error: List index is out of range")

except TypeError:
    print("Error: Wrong data type used")

finally:
    print("Program finished")