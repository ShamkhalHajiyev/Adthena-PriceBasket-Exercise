class Basket:
    PRICES = {
        "Soup": 0.65,
        "Bread": 0.80,
        "Milk": 1.30,
        "Apples": 1.00
    }

    def __init__(self, items):
        self.items = items
        self.product_count = self._count_products()

    def _count_products(self):
        # Count occurrences of each product
        count = {}
        for item in self.items:
            if item in count:
                count[item] += 1
            else:
                count[item] = 1
        return count

    def calculate_subtotal(self):
        # Calculate subtotal for all items in the basket
        return sum(self.PRICES[item] * self.product_count[item] for item in self.product_count)
