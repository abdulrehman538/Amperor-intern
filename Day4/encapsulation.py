class BankAccount:
    def __init__(self, name, balance):
        # PUBLIC ATTRIBUTE (can be accessed directly)
        self.name = name

        # PROTECTED / HIDDEN ATTRIBUTE (encapsulation concept)
        # We use "_" to show: "do not touch directly"
        self._balance = balance

    # -------------------------------
    # GETTER METHOD (READ ONLY ACCESS)
    # -------------------------------
    def get_balance(self):
        # This method allows safe reading of balance
        # We do NOT give direct access to _balance
        return self._balance

    # -------------------------------
    # DEPOSIT METHOD (CONTROLLED UPDATE)
    # -------------------------------
    def deposit(self, amount):
        # Check if amount is valid
        if amount > 0:
            # Update hidden balance safely
            self._balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Invalid deposit amount")

    # -------------------------------
    # WITHDRAW METHOD (CONTROLLED UPDATE)
    # -------------------------------
    def withdraw(self, amount):
        # Check two conditions:
        # 1. amount must be positive
        # 2. enough balance must be available
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"Withdrawn: {amount}")
        else:
            print("Invalid withdrawal or insufficient balance")


# ===============================
# CREATE OBJECT (REAL ACCOUNT)
# ===============================
account = BankAccount("Abdul", 1000)

# -------------------------------
# ACCESS PUBLIC DATA DIRECTLY
# -------------------------------
print("Account Holder:", account.name)

# -------------------------------
# ACCESS PRIVATE DATA VIA GETTER
# -------------------------------
print("Initial Balance:", account.get_balance())  # SAFE ACCESS

# -------------------------------
# DEPOSIT MONEY (CONTROLLED)
# -------------------------------
account.deposit(500)

# -------------------------------
# WITHDRAW MONEY (CONTROLLED)
# -------------------------------
account.withdraw(300)

# -------------------------------
# FINAL BALANCE CHECK
# -------------------------------
print("Final Balance:", account.get_balance())