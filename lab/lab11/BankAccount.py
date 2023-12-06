class BankAccount:
    def __init__(self, accountID='', balance=0):
        self.a = accountID
        self.b = balance

    def set_account_ID(self, newID):
        self.a = newID

    def set_balance(self, new_balance):
        self.b = new_balance

    def get_account_ID(self):
        return self.a

    def get_balance(self):
        return self.b

    def deposit(self, amount):
        self.b += amount

    def withdrawal(self, amount):
        self.b -= amount

    def __str__(self):
        return f"ID: {self.a}, Balance: {self.b:.2f}"


account = BankAccount("1001", 500)

while True:
    choice = int(
        input("Deposit (1), Withdrawal (2), Update (3), or Exit (0): "))
    if choice == 0:
        break
    elif choice == 1:
        amount = float(input("Enter your deposit amount: "))
        account.deposit(amount)
        print(account)
    elif choice == 2:
        amount = float(input("Enter your withdrawal amount: "))
        account.withdrawal(amount)
        print(account)
    else:
        amount = float(input("Enter your update amount: "))
        account.set_balance(amount)
        print(account)
