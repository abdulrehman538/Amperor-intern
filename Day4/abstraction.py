from abc import ABC, abstractmethod

class Calculator(ABC):

    @abstractmethod
    def calculate(self, a, b):
        pass

    @abstractmethod
    def display(self, result):
        pass


class AddCalculator(Calculator):

    def calculate(self, a, b):
        return a + b


class SubtractCalculator(Calculator):

    def calculate(self, a, b):
        return a - b


class MultiplyCalculator(Calculator):

    def calculate(self, a, b):
        return a * b


class DivideCalculator(Calculator):

    def calculate(self, a, b):
        if b == 0:
            return "Error: Division by zero"
        return a / b


# ------------------ MAIN PROGRAM ------------------

print("Select Operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice (1/2/3/4): ")

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if choice == '1':
    calc = AddCalculator()
elif choice == '2':
    calc = SubtractCalculator()
elif choice == '3':
    calc = MultiplyCalculator()
elif choice == '4':
    calc = DivideCalculator()
else:
    print("Invalid choice")
    exit()

result = calc.calculate(a, b)

print("Result:", result)