import unittest
from shoppinCart import ShoppingCart
from product import Product
class TestShoppingCart(unittest.TestCase):
        def test_addProduct(self):
            cart = ShoppingCart()
            product = Product('Apple', 10, 5)
            cart.addProduct(product)
            self.assertEqual(cart.products[0].name, 'Apple')
        def test_calculateTotal_empty_cart(self):
            cart = ShoppingCart()
            self.assertEqual(cart.calculateTotal(), 0)
        def test_calculateTotal_with_product(self):
            cart = ShoppingCart()
            product = Product('Apple', 10, 5)
            cart.addProduct(product)
            self.assertEqual(cart.calculateTotal(), 50)
if __name__ == '__main__':
    unittest.main()
        