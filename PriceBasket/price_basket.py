import sys
from basket import Basket
from offers import apply_offers


def main():
    # Ensure the command-line argument is provided
    if len(sys.argv) < 2:
        print("Please provide a list of products.")
        return

    # Extract products from command line arguments
    products = sys.argv[1:]

    # Create a basket and calculate subtotal
    basket = Basket(products)
    subtotal = basket.calculate_subtotal()

    # Apply offers and get total
    discounts, total = apply_offers(basket)

    # Print output
    print(f"Subtotal: £{subtotal:.2f}")
    if discounts:
        for discount, amount in discounts.items():
            print(f"{discount}: {amount:.2f}p")
    else:
        print("(No offers available)")

    print(f"Total: £{total:.2f}")


if __name__ == "__main__":
    main()
