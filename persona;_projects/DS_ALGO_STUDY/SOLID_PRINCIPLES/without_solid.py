class Order:

    """
    Order class should not handle payment here



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
            total +=i
        return total

    def pay(self, payment_type, security_code):
        if payment_type == "debit":
            print("debit type")
            self.status = "paid"
        elif payment_type == "credit":
            print("credit type")
            self.status = "paid"
        else:
            raise Exception(f"Unknown payment type :{payment_type}")

order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB", 2, 5)
print(order.total_price())
order.pay("debit", "xyz")
