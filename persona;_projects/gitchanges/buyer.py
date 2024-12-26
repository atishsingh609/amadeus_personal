from pyb.tracer import trace, DEBUG
from uuid import uuid4


class Buyer:
    def __init__(self, container):
        """
        :param container: Proto container
        """
        self.container = container
        self._data = self.build_buyer()

    def get_data(self):
        return self._data

    def set_data(self, value):
        self._data = value

    data = property(get_data, set_data)

    def build_buyer(self):
        """
        Get the buyer details.
        return: Buyer contact information.
        """
        buyer = dict()
        email = "None"
        phone_number = "None"
        for contact in self.container.contacts_objects_dict.values():
            if contact.refids:
                continue
            else:
                if contact.email and contact.email.value:
                    email = contact.email.value
                if contact.telephone and contact.telephone.value:
                    phone_number = contact.telephone.value
        buyer["contacts"] = {"emailAddress": [{"category": "OTHER", "address": email}],
                             "phonenumbers": [{"category": "OTHER", "number": phone_number}]}
        buyer["roles"] = ["BUYER"]
        buyer["id"] = str(uuid4())
        trace(DEBUG, f" Buyer details is {buyer}")
        return buyer


