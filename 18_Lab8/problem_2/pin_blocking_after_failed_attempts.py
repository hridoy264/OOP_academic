class GoodBankAccount:
    
    def __init__(self, account_holder, balance, pin):
        self.account_holder = account_holder
        self.__balance = balance
        self.__pin = pin
        self.wrong_attempt = 0

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
    def check_balance(self, entered_pin):
        if entered_pin == self.__pin:
            print(f"Current balance: {self.__balance}")
            self.wrong_attempt = 0
        else:
            print("Wrong pin, access denied :(")
            self.wrong_attempt += 1
            if self.wrong_attempt > 3:
                print("Too many wrong attemps! Account is blocked :(")

secure_account = GoodBankAccount("Hridoy", 10000, 123)

secure_account.deposit(2000)
secure_account.check_balance(123)
secure_account.withdraw(4000)
secure_account.check_balance(1234)
secure_account.withdraw(23000)

# I will try to modify balance outside of the class, let's see what happen!
secure_account.__balance = -3000
secure_account.check_balance(123)

secure_account.withdraw(500)
secure_account.check_balance(1223)
secure_account.check_balance(23432)
secure_account.check_balance(234)
secure_account.check_balance(342)
print(f"Number of wrong attempt: {secure_account.wrong_attempt}")

secure_account.check_balance(123)
print(f"Number of wrong attempt: {secure_account.wrong_attempt}")
