from pyb.tracer import trace, DEBUG
from uuid import uuid4


class Actor:
    def __init__(self, container, actor_object):
        """
        :param container: proto container
        :param actor_object: Actor object dict
        """
        self.container = container
        self.actor_object = actor_object
        self.actor_uid = actor_object.uid
        self._data = self.build_actors()

    def get_data(self):
        return self._data

    def set_data(self, value):
        self._data = value

    data = property(get_data, set_data)

    def build_actors(self):
        """
        It will prepare the travellers details.
        :return: Actor node.
        """
        trace(DEBUG, f"Actor object  {self.actor_object}")
        actor = dict()
        actor["orderItemIds"] = []
        email, phone_number = self.get_actor_contact(self.actor_uid)
        actor["contact"] = {"emailAddress": email,
                            "phoneNumbers": [{"category": "OTHER",
                                              "number": phone_number}]}
        actor["dateOfBirth"] = self.actor_object.date_of_birth
        actor["id"] = self.actor_uid
        actor["role"] = ["Traveler"]
        actor["firstName"] = self.actor_object.name[0].first_name
        actor["lastName"] = self.actor_object.name[0].last_name
        return actor

    def get_actor_contact(self, actor_id):
        """
        Check if actor has Email and Telephone number.
        :param actor_id: ID of actor, for which we get contacts
        :return: Contact for the actor if present otherwise return NA.
        """
        email = "None"
        telephone = "None"
        for contact in self.container.contacts_objects_dict.values():
            if actor_id in contact.refids:
                if contact.email and contact.email.value:
                    email = contact.email.value
                if contact.telephone and contact.telephone.value:
                    telephone = contact.telephone.value
        return email, telephone


