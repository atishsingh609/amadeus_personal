class Order:
    """
    Now Order has only responsibility of order.

    """
    items = []
    quant = []
    price = []
    status = "open"

    def add_item(self, name, qunat, price):
        self.items.append(name)
        self.quant.append(price)
        self.price.append(price)

    def total_price(self):
        total = 0
        for i in self.price:
            total += i
        return total


class PaymentProcessor:
    """
    If new payment method like bitcoine then this class need to be modified.
    So, it doesnot follow open/closed principle.

    """

    def pay_debit(self, order):
        print("debit type")
        self.status = "paid"
    def pay_credit(self, order):
        print("credit type")
        self.status = "paid"



order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB", 2, 5)
print(order.total_price())
order.pay("debit", "xyz")
