from uuid import uuid4
from .accomodation import Accommodation
from pyb.tracer import trace, INFO, ERROR, DEBUG
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
            self.reservation["creatorOfficeId"] = office_id
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
        trace(DEBUG, f"Encoded Actors details is {actors}")
        return actors

    def get_accommodations(self):
        accommodations = []

        for accommodation_id in self.container.accommodation_objects_dict:
            accommodation = Accommodation(self.bom, self.container, accommodation_id)
            if accommodation.data:
                accommodations.append(accommodation.data)
        trace(DEBUG, f"Encoded accommodations {accommodations}")

        return accommodations

    def get_total_price(self):
        total_price = dict()
        total_price["total"] = ""
        total_price["currency"] = ""
        for _, product in self.container.products_objects_dict.items():
            if product.price[0].price_type and product.price[0].price_type == "Total":
                total_price["total"] = product.price[0].amount
                total_price["currency"] = product.price[0].currency_code
                break
        trace(DEBUG, f"Total price is {total_price}")
        return total_price

    def get_ticket_options(self):
        ticket_option = []
        part_ticket_option = dict()
        part_ticket_option["ticketType"] = ""
        part_ticket_option["selected"] = False
        for _, tkt_opt in self.container.ticketing_option_objects_dict.items():
            part_ticket_option["ticketType"] = tkt_opt.attributes.get("Type")
            if tkt_opt.attributes.get("PreAssigned") == "1":
                part_ticket_option["selected"] = True
            ticket_option.append(part_ticket_option)
        trace(DEBUG, f"Encoded Ticket option is {ticket_option}")
        return ticket_option

    def get_ticket_time_limit(self):
        ticket_time_limit = dict()
        ticket_time_limit["effectiveTicketTimeLimit"] = ""
        ticket_time_limit["overridden"] = False
        ticket_time_limit["overrideAllowed"] = False
        for _, product in self.container.products_objects_dict.items():
            if product.ticket_expiration_type:
                ticket_time_limit["effectiveTicketTimeLimit"] = product.ticket_expiration_type
                ticket_time_limit["technicalTicketTimeLimit"] = product.ticket_expiration_type
                break
        return ticket_time_limit

    def get_itinerary(self):
        itinerary = []
        return itinerary

    def get_admissions(self):
        admission = []
        return admission

    def get_orderitems(self):
        itinerary = self.get_itinerary()
        admission = self.get_admissions()
        accommodations = self.get_accommodations()
        total_price = self.get_total_price()
        direction = ""
        obj = [{
            "id": str(uuid4()),
            "itinerary": itinerary,
            "admissions": admission,
            "accommodations": accommodations,
            "totalPrice": total_price,
            "direction": direction}]
        return obj

    def _build_reservation(self):
        """
        :return: offer dictionary containing the itinerary.
        """
        self.actors = self.get_actors()
        self.orderitems = self.get_orderitems()
        reservation = {"actors": self.actors,
                       "orderItems": self.orderitems,
                       "totalPrice": self.get_total_price(),
                       "pnrRecordLocator": "KDU67S",
                       "ticketingOptions": self.get_ticket_options(),
                       # "creatorOfficeId": "BRN2S78AB",
                       "ticketTimeLimit": self.get_ticket_time_limit(),
                       "id": str(uuid4())}
        return reservation



