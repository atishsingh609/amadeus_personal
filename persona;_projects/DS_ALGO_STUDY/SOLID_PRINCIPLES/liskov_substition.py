"""
The Liskov Substitution Principle (LSP) is a fundamental principle in object-oriented programming
 that states that objects of a superclass should be able to be replaced with objects of a
 subclass without affecting the correctness of the program.


"""

from abc import ABC, abstractmethod


class ProcessPayment(ABC):
    @abstractmethod
    def pay(self, order):
        pass


class DebitCardPay(ProcessPayment):

    def __init__(self, security_code):
        self.security_code = security_code

    def pay(self, order):
        print("process debit card payment")


class CreditCardPay(ProcessPayment):

    def __init__(self, security_code):
        self.security_code = security_code

    def pay(self, order):
        print("process credit card payment")


class PaypalPay(ProcessPayment):
    def __init__(self, email_address):
        self.security_code = email_address

    def pay(self, order):
        print("process bit coin payment")
