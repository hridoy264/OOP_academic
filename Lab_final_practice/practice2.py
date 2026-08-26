class SecureAccount:
    def __init__(self, name, balance, pin):
        self.name=name
        self.__balance=balance
        self.__pin= pin
        self.__attempt=0
        self.__blocked=False

    def show_balance(self):
        pass