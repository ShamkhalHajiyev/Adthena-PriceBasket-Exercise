import unittest
from basket import Basket

class TestBasket(unittest.TestCase):
    def test_subtotal(self):
        basket = Basket(['Soup', 'Bread', 'Milk'])
        self.assertEqual(basket.calculate_subtotal(), 2.75)

    def test_empty_basket(self):
        basket = Basket([])
        self.assertEqual(basket.calculate_subtotal(), 0)

if __name__ == '__main__':
    unittest.main()
