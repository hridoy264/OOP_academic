class BankAccount:
    def __init__(self, name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, deposit_amount):
        self.balance += deposit_amount
        print(f"{deposit_amount} bdt successfully deposited!")

    def withdrowal(self, withdraw_amount):
        self.balance -= withdraw_amount
        print(f"{withdraw_amount} bdt has been withdraw")

    def bankFees(self):
        self.balance = self.balance - .05*self.balance

    def display(self):
        print("Current Balance: ", self.balance)

acc1 = BankAccount('Shahnewaj', 264, 30000)
acc1.display()
acc1.deposit(10000)
acc1.withdrowal(500)
acc1.display()