class Product:
    def __init__(self, name, price,quantity=0):
        self.name = name
        self.price = price
        if quantity < 0:
            raise ValueError('Quantity cannot be negative')
        self.quantity = quantity

    def calculate(self):
        if self.quantity < 0:
            raise ValueError('Quantity cannot be negative')
        return self.price * self.quantity


