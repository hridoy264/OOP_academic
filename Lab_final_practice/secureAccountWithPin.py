class PinBankAccount:
    def __init__(self, account_holder, balance, pin):
        self.account_holder = account_holder
        self.__balance = balance        # private variable
        self.__pin = pin

    def deposit(self, amount):
        self.__balance += amount
        print(f"Successfully deposited {amount} bdt")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Successfully withdraw {amount} bdt")
        else:
            print("Not sufficient balance!")

    def check_balance(self, enterd_pin):
        if enterd_pin == self.__pin:
            print(f"Your current balance is {self.__balance} bdt")
        else:
            print("Wrong pass")

pinbank = PinBankAccount("Shahnewaj Hridoy", 10000, 264)
pinbank.deposit(500)
pinbank.withdraw(4000)
# It is not affecting balance value at all
pinbank.__balance = 90
pinbank.check_balance(123)
pinbank.check_balance(264)




