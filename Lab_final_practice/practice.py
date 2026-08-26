class SecureAccount:
    def __init__(self, name, balance, pin):
        self.name=name
        self.__balance=balance
        self.__pin=pin
        self.__attempt=0

    def check_balance(self, entered_pin):
        if entered_pin==self.__pin:
            print(f"Current balance: {self.__balance}")
        else:
            self.__attempt+=1
            print(f"Wrong attempt! Wrong attempt: {self.__attempt}")

    def deposit(self, amount):
        if amount>0:
            self.__balance+=amount

    def withdraw(self, amount, entered_pin):
        if entered_pin==self.__pin:
            if amount<=self.__balance:
                self.__balance-=amount

            else:
                print(f"Insufficient balance")

        else:
            self.__attempt+=1
            print(f"wrong attempt: {self.__attempt}")

user=SecureAccount("Shah",1000, 9091)
user.deposit(2000)
user.withdraw(1500, 1000)
user.withdraw(1500, 1020)
user.withdraw(1500, 1200)
user.withdraw(1300, 9091)
user.check_balance(9091)

