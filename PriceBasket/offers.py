def apply_offers(basket):
    discounts = {}
    subtotal = basket.calculate_subtotal()
    total = subtotal

    # Apples 10% discount
    if "Apples" in basket.product_count:
        discount_apples = 0.1 * basket.PRICES["Apples"] * basket.product_count["Apples"]
        total -= discount_apples
        discounts["Apples 10% off"] = discount_apples * 100  # Display as pence

    # Buy 2 Soups, get Bread half price
    if "Soup" in basket.product_count and "Bread" in basket.product_count:
        num_soup = basket.product_count["Soup"]
        num_bread = basket.product_count["Bread"]
        discount_bread = min(num_soup // 2, num_bread) * 0.5 * basket.PRICES["Bread"]
        total -= discount_bread
        if discount_bread > 0:
            discounts["Buy 2 Soups, get Bread half price"] = discount_bread * 100  # Display as pence

    return discounts, total
