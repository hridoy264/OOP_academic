class GoodBankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance        # private variable

    def deposit(self, amount):
        self.__balance += amount
        print(f"Successfully deposited {amount} bdt")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Successfully withdraw {amount} bdt")
        else:
            print("Not sufficient balance!")

    def check_balance(self):
        print(f"Your current balance is {self.__balance} bdt")

goodbank = GoodBankAccount("Shahnewaj Hridoy", 10000)
goodbank.deposit(500)
goodbank.withdraw(4000)
# It is not affecting balance value at all
goodbank.__balance = 90
goodbank.check_balance()




