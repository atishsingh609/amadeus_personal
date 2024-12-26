from uuid import uuid4
from pyb.tracer import trace, DEBUG
from .buyer import Buyer
from .actor import Actor


class EncodeReservation:
    """
    This class has the scope to encode the payload of the PUT/reservation.
    At the moment this implementation is in progress.
    """
    def __init__(self, container, bom, language, office_id, distributor_id, current_provider, transaction_id=None):
        self.container = container
        self.bom = bom
        self.actors = []
        self.orderitems = []
        self.provider = current_provider
        if transaction_id:
            self.transaction_id = transaction_id
        else:
            self.transaction_id = str(uuid4())
        self.reservation = self._build_reservation()
        if language:
            self.reservation["language"] = language
        else:
            self.reservation["language"] = "EN"
        if office_id:
            self.reservation["officeId"] = office_id
        if distributor_id:
            self.reservation["distributor"] = distributor_id
        trace(DEBUG, "reservation %s" % self.reservation)

    def get_actors(self):
        """
        This will call the Actor and buyer class to prepare Actor filed.
        :return: Actor dictionary.
        """
        actors = []
        for _, val in self.container.actors_objects_dict.items():
            actor = Actor(self.container, val)
            actors.append(actor.data)
        buyer = Buyer(self.container)
        actors.append(buyer.data)
        trace(DEBUG, f"Actors details is {actors}")
        return actors

    def _build_reservation(self):
        """
        :return: offer dictionary containing the itinerary.
        """
        self.actors = self.get_actors()
        # self.orderitems = self.get_orderitems()
        reservation = {"actors": self.actors,
                       "itinerary": self.orderitems,
                       "id": self.transaction_id}
        return reservation
