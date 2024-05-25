class BankAccount:
    def __init__(self, account_number):
        self.balance = 0
        self.account_number = account_number

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.balance

    def get_account_number(self):
        return self.account_number

# Example usage
account = BankAccount("123456")
account.deposit(100)
print(account.get_balance())  
account.withdraw(50)
print(account.get_balance())
print(account.get_account_number())  
