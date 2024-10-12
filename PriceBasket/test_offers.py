import unittest
from basket import Basket
from offers import apply_offers

class TestOffers(unittest.TestCase):
    def test_apple_discount(self):
        basket = Basket(['Apples'])
        discounts, total = apply_offers(basket)
        self.assertIn('Apples 10% off', discounts)
        self.assertEqual(total, 0.90)

    def test_soup_bread_offer(self):
        basket = Basket(['Soup', 'Soup', 'Bread'])
        discounts, total = apply_offers(basket)
        self.assertIn('Buy 2 Soups, get Bread half price', discounts)
        self.assertEqual(total, 1.70)

    def test_no_offers(self):
        basket = Basket(['Milk'])
        discounts, total = apply_offers(basket)
        self.assertEqual(discounts, {})
        self.assertEqual(total, 1.30)

if __name__ == '__main__':
    unittest.main()
