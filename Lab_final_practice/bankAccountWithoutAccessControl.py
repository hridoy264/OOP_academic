class BadBankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, deposit_amount):
        self.balance += deposit_amount
        print(f"Successfully deposited {deposit_amount}. Your current balance is {self.balance}")

    def withdraw(self, withdrawal_ammount):
        if withdrawal_ammount < self.balance:
            self.balance -= withdrawal_ammount
            print(f"Succesfully withdraw {withdrawal_ammount}. Your current balance is {self.balance}") 
        else:
            print("Not sufficient amount!")

badbank = BadBankAccount("Shahnewaj Hriody", 10000)
badbank.deposit(5000)
badbank.withdraw(300)
badbank.withdraw(40000)

