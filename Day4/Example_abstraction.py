from abc import ABC, abstractmethod

class BankSystem(ABC):

    @abstractmethod
    def deposit(self, balance):
        pass

    @abstractmethod
    def withdraw(self, balance):
        pass


class DepositAmount(BankSystem):

    def deposit(self, balance):
        return balance + balance

    def withdraw(self, balance):
        pass


print("Welcome to the Bank System")
print("1. Deposit")
print("2. withdraw")

choice = input("Enter what you want(1/2): ")

if choice == '1':
    a = int(input("Enter your amount you want to deposit: "))
    obj = DepositAmount()
    result = obj.deposit(balance=a)
    print("Your Total Amount:", result)

elif choice == '2':
    print("Not functioned yet")

else:
    print("Invalid Input")