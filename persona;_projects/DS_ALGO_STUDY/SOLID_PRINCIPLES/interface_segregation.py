"""
To make below code to follow interface segregation,

we need to make different interface for payment and auth
because some class mey need different type of auth process.
We can resolve this by making a new auth interface.

"""

from abc import ABC, abstractmethod


class SmsAuth:
    auth = False

    def verify_code(self, code):
        print("verifying code")
        self.auth = True

    def is_auth(self, code):
        self.verify_code(code)
        return self.auth


class ProcessPayment(ABC):
    @abstractmethod
    def pay(self, order):
        pass


class DebitCardPay(ProcessPayment):

    def __init__(self, security_code, auth: SmsAuth):
        self.security_code = security_code
        self.auth = auth

    def pay(self, order, ):
        if self.auth.is_auth(self.security_code):
            print("process debit card payment")


class CreditCardPay(ProcessPayment):

    def __init__(self, security_code):
        self.security_code = security_code

    def pay(self, order):

        print("process credit card payment")


class PaypalPay(ProcessPayment):
    def __init__(self, email_address, auth:SmsAuth):
        self.security_code = email_address
        self.auth = auth

    def pay(self, order):
        if self.auth.is_auth(self.security_code):
            print("process bit coin payment")

"""



"""