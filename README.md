# PriceBasket

This project calculates the price of a basket of products, applying any special offers that are available.

## Products and Pricing

- **Soup**: 65p per tin.
- **Bread**: 80p per loaf.
- **Milk**: £1.30 per bottle.
- **Apples**: £1.00 per bag.

## Special Offers

- **Apples**: 10% off their normal price this week.
- **Buy 2 tins of Soup, get 1 loaf of Bread half price.**

## Prerequisites

- Python version > 3.8 is required.
  
You can check your Python version with:

```bash
python --version
```

## Setup Instructions

1. **Clone the Repository**:

   Clone the repository to your local machine by running the following command:

   ```bash
   git clone https://github.com/ShamkhalHajiyev/Adthena-Python-Analyst-Coding-Exercise
   ```

   Replace `https://github.com/ShamkhalHajiyev/Adthena-Python-Analyst-Coding-Exercise` with the URL of your GitHub repository.

2. **Navigate to the Project Directory**:

   After cloning, navigate to the project directory:

   ```bash
   cd Adthena-Python-Analyst-Coding-Exercise/PriceBasket
   ```

3. **Install Python Dependencies (if any)**:

   There are no additional dependencies required beyond standard Python. However, if you plan to install testing or code formatting tools, you can do so with `pip`.

4. **Running the Program**:

   To calculate the price of a basket of products, you can run the program via the command line. 

   The command format is as follows:

   ```bash
   python price_basket.py product1 product2 product3 ...
   ```

   ### Example:

   ```bash
   python price_basket.py Apples Milk Bread
   ```

   The output will show the subtotal, applicable discounts, and the total price:

   ```
   Subtotal: £3.10
   Apples 10% off: 10.00p
   Total: £3.00
   ```

5. **Running Tests**:

   This project includes unit tests to ensure correctness. To run the tests, execute the following command:

   ```bash
   python -m unittest discover
   ```

   This will run all the unit tests in the `test_basket.py` and `test_offers.py` files.

## Project Structure

- `price_basket.py`: Main entry point for the command-line interface. It accepts the list of products, calculates the subtotal, applies offers, and prints the results.
  
- `basket.py`: This module contains the `Basket` class, which is responsible for holding the products, counting their quantities, and calculating the subtotal.

- `offers.py`: This module contains the logic for applying special offers. It calculates applicable discounts and adjusts the total price accordingly.

- `test_basket.py`: Unit tests for the `Basket` class, ensuring correct product counting and subtotal calculation.

- `test_offers.py`: Unit tests for the `apply_offers` function, ensuring discounts and total price calculations work as expected.

## Example Usage

Here are some examples of how to use the program:

### Example 1:

```bash
python price_basket.py Soup Soup Bread
```

Output:
```
Subtotal: £2.10
Buy 2 Soups, get Bread half price: 40.00p
Total: £1.70
```

### Example 2:

```bash
python price_basket.py Apples Milk
```

Output:
```
Subtotal: £2.30
Apples 10% off: 10.00p
Total: £2.20
```

### Example 3:

```bash
python price_basket.py Milk
```

Output:
```
Subtotal: £1.30
(No offers available)
Total: £1.30
```

## Design Decisions

- **Separation of Concerns**: 
  - The product and subtotal calculation logic is kept in `basket.py`, while the special offer calculations are handled in `offers.py`. This separation ensures that the code remains modular and easy to extend.
  
- **Extensibility**: 
  - New products or special offers can be easily added without significant modifications to the existing code. For instance, if a new product is introduced or a new offer is applied, you can simply update the relevant sections of the code without affecting the rest.

- **Unit Testing**: 
  - Unit tests have been written to verify the functionality of both the basket pricing and the application of special offers. This ensures that the program behaves as expected, even if changes are made to the code in the future.

## Potential Enhancements

- **Internationalization**: If the system were to support multiple currencies or regions, additional formatting and conversion logic would be required.
  
- **Additional Offers**: It would be easy to extend the offers system to support more complex discount rules or loyalty programs.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
