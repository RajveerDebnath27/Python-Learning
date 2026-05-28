# Create a class called BankAccount.
# It should take an owner_name and a starting balance when you create it.
# It should have a method called deposit(amount) that adds money to the balance.
# It should have a method called withdraw(amount) that subtracts money from the balance.

class BankAccount:
    def __init__(self, account_name, balance):
        self.account_name = account_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount



B1 = BankAccount("Apurba Debnath", 10000)
print(B1.account_name, B1.balance)
B1.deposit(int(input("Deposit amount:")))
print(B1.account_name, B1.balance)
B1.withdraw(int(input("Withdraw amount:")))
print(B1.account_name, B1.balance)