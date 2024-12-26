import string
import random
from typing import List

def generate_id(length=8):
    return ''.join(random.choice(string.ascii_uppercase))


class SupportTicket:
    id: str
    customer: str
    issue: str

    def __init__(self, customer, issue):
        self.id = generate_id()
        self.customer = customer
        self.issue = issue


class CustomerSupport:

    tickets: List[SupportTicket] = []

    def create_ticket(self, customer, issue):
        self.tickets.append(SupportTicket(customer, issue))

    def process_tickets(self, procession_strategy : str = "fifo"):
        if len(self.tickets) == 0:
            print("There are no ticketts to process")
            return

        if procession_strategy == "fifo":
            for ticket in self.tickets:
                self.process_tickets(ticket)
        elif procession_strategy == "filo":
            for ticket in reversed(self.tickets):
                self.process_tickets(ticket)

        elif procession_strategy == "random":
            list_copy = self.tickets.copy()
            random.shuffle(list_copy)
            for ticket in list_copy:
                self.process_tickets(ticket)

    def process_ticket(self, ticket: SupportTicket):
        print("=============================")
        print(f"processing ticket id : {ticket.id}")
        print(f"customer : {ticket.customer}")
        print(f"issue : {ticket.issue}")

app = CustomerSupport()
app.create_ticket("atish", "some issue 1")
app.create_ticket("atish2", "some issue 2 ")
app.create_ticket("atish3", "some issue 3")
app.create_ticket("atish5", "some issue 4")

app.process_tickets("fifo")



"""
we shpuld create different class for different ticketing strategy

"""

from abc import ABC, abstractmethod

class TicketingOrderingStrategy:

    @abstractmethod
    def create_ordering(self, list: List[SupportTicket]) -> List[SupportTicket]:
        pass


class FIFOTicketingStrategy(TicketingOrderingStrategy):

    def create_ordering(self, list):
        return list.copy()


class FILOTicketingStrategy(TicketingOrderingStrategy):

    def create_ordering(self, list):
        return reversed(list)


class RandomTicketingStrategy(TicketingOrderingStrategy):

    def create_ordering(self, list):
        return list.copy()


"""
Now instead of passing strategy as string we can pass object of this class and use 
function inside that to order tickets. 


we can also go for function approcach by creating different function based on different 
strategy to be implemented.

"""