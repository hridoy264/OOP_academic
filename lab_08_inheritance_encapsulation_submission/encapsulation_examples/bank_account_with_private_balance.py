class GoodBankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance
    def deposit(self, deposit_amount):
        if deposit_amount < 0:
            print("Deposit amount must have to be positive")
        self.__balance += deposit_amount
        print(f"{deposit_amount} successfully deposited")
    def withdraw(self, withdraw_amount):
        if withdraw_amount>self.__balance:
            print("You have not sufficient balance :(")
        else:
            self.__balance -= withdraw_amount
            print(f"{withdraw_amount} successfully withraw")
    def check_balance(self):
        print(f"Current balance: {self.__balance}")

good_account = GoodBankAccount("Hridoy", 10000)

good_account.deposit(2000)
good_account.check_balance()
good_account.withdraw(4000)
good_account.check_balance()
good_account.withdraw(23000)

# I will try to modify balance outside of the class, let's see what happen!
good_account.__balance = -3000
good_account.check_balance()

good_account.withdraw(500)
good_account.check_balance()