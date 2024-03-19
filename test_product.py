import unittest
from product import Product
class Testproducts(unittest.TestCase):
    def test_productsTotal_positive(self):
        products = Product('Apple', 10, 5)
        self.assertEqual(products.calculate(), 50)
    def test_product_negative_quantity(self):
        with self.assertRaises(ValueError):
            products = Product('Apple', 10, -5)
    def test_product_negative_quantity(self):
        products = Product('Apple', 10, -5)
        self.assertRaises(ValueError, products.calculate)
    def test_product_negative_quantity(self):
        products = Product('Apple', 10, -5)
        self.assertRaises(ValueError, products.calculate)
    def test_product_negative_quantity(self):
        products = Product('Apple', 10, -5)
        self.assertRaises(ValueError, products.calculate)
    def test_product_negative_quantity(self):
        products = Product('Apple', 10, -5)
        self.assertRaises(ValueError, products.calculate)
            
    def test_productsTotal_zero(self):
        products = Product('Apple', 10, 0)
        self.assertEqual(products.calculate(), 0)
if __name__ == '__main__':
    unittest.main()