class BadBankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
    def deposit(self, deposit_amount):
        self.deposit_amount = deposit_amount
        self.balance += self.deposit_amount
    def withdraw(self, withdraw_amount):
        self.withdraw_amount = withdraw_amount
        if self.withdraw_amount>self.balance:
            print("You have not sufficient balance :(")
        else:
            self.balance -= self.withdraw_amount

bad_account = BadBankAccount("Hridoy", 10000)
print(bad_account.balance)
bad_account.deposit(2000)
print(bad_account.balance)
bad_account.withdraw(4000)
print(bad_account.balance)
bad_account.withdraw(23000)