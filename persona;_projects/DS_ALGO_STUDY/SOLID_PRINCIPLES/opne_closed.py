"""
Class should be open for extensation but closed for mofidications


This code satisfies open closed but nor Liscov principle.

The Liskov Substitution Principle (LSP) is a fundamental principle in
object-oriented programming that states that objects of a
superclass should be able to be replaced with objects of a
subclass without affecting the correctness of the program.


but here suppose paypal uses a different type of security than other two then
this need to handle differently and code need to be changed.
"""

from abc import ABC, abstractmethod


class ProcessPayment(ABC):
    @abstractmethod
    def pay(self, order, security_code):
        pass


class DebitCardPay(ProcessPayment):

    def pay(self, order, security_code):
        print("process debit card payment")


class CreditCardPay(ProcessPayment):

    def pay(self, order, security_code):
        print("process credit card payment")


class PaypalPay(ProcessPayment):

    def pay(self, order, security_code):
        print("process bit coin payment")


debit = DebitCardPay()
debit.pay()
credit = CreditCardPay()
credit.pay()
debit = PaypalPay()
debit.pay()
