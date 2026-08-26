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
        # print(f"The payment of {self.total} is processed by credit Card. The transection fee is {self.deduct}")
        print(f"Processing Credit Card (ending {self.card_number%10000}). Amount: ${self.total}, Fee: ${self.deduct}, Net: ${self.total + self.deduct}")

class PayPalPayment(Payment):
    def __init__(self, email):
        super().__init__()
        self.email = email 

    def process_payment(self, total):
        self.total = total
        self.deduct = self.total * 0.01
        # print(f"The payment of {self.total} is processed by PayPal Payment. The transection fee is {self.deduct}")
        print(f"Processing PayPal ({self.email}). Amount: ${self.total}, Fee: ${self.deduct}, Net: ${self.total + self.deduct}")


class CashPayment(Payment):
    def __init__(self):
        super().__init__()


    def process_payment(self, total):
        self.total = total
        # print(f"The payment of {self.total} is a Cash Payment.")
        print(f"Processing Cash. Amount: ${self.total}, No Fee")


pay1 = CreditCardPayment(2187980703, 234, 324)
pay2 = PayPalPayment("hridoyq264@gmail.com")
pay3 = CashPayment()

payment_objects = [pay1, pay2, pay3]

if __name__=="__main__":

    def checkout_payment(payment_method, total):
        payment_method.process_payment(total)

    # checkout_payment(pay1, 3000323)
    # checkout_payment(pay2, 2349)
    # checkout_payment(pay3, 2439)

    for i in payment_objects:
        i.process_payment(100)
