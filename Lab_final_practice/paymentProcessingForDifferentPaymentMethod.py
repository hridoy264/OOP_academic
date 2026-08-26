class Payment:
    def __init__(self):
        pass
    def process_payment(self):
        pass

class CreditCardPayment(Payment):
    def __init__(self, card_number, expiry, cvv):
        super().__init__()
        self.card_number = card_number
        self.expiry = expiry
        self.cvv = cvv

    def process_payment(self, total):
        self.total = total
        self.deduct = self.total * 0.02
        print(f"The payment of {self.total} is processed by credit Card. The transection fee is {self.deduct}")

class PayPalPayment(Payment):
    def __init__(self, email):
        super().__init__()
        self.email = email 

    def process_payment(self, total):
        self.total = total
        self.deduct = self.total * 0.01
        print(f"The payment of {self.total} is processed by PayPal Payment. The transection fee is {self.deduct}")

class CashPayment(Payment):
    def __init__(self):
        super().__init__()


    def process_payment(self, total):
        self.total = total
        print(f"The payment of {self.total} is a Cash Payment.")

pay1 = CreditCardPayment(213, 234, 324)
pay2 = PayPalPayment("hridoyq264@gmail.com")
pay3 = CashPayment()


def checkout_payment(payment_method, total):
    payment_method.process_payment(total)

checkout_payment(pay1, 3000)

