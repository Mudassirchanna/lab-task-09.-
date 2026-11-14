# LAB_TASK
"""Q:NO:04 create a class named bankaccount.
initialize account_hodler  and balace.
create a method deposite() to ad money. 
create a method display_balance. """
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance")

    def display_balance(self):
        print("Account Holder:", self.account_holder)
        print("Balance:", self.balance)


account = BankAccount("Mudassir", 5000)

account.deposit(2000)
account.withdraw(1000)
account.display_balance() 