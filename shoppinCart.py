class ShoppingCart:
    def __init__(self):
        self.products = []
    def addProduct(self, product):
        self.products.append(product)
    def calculateTotal(self):
        return sum([product.calculate() for product in self.products])