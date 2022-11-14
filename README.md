Adthena Python Analyst Coding Exercise
Write a program driven by unit tests that can price a basket of products taking into account some special
offers. The program should demonstrate your knowledge of clean extendible code.
● Please use Python > 3.8
● Please include a readme.md file with instructions on how to set up and run your code
● Please include any comments about your code, decisions made that you feel may be relevant
● Please submit your code via a GitHub repo
● Please do not use the word “adthena” in your GitHub repo name
Coding Exercise:
Products that can be purchased, together with their prices are:
● Soup – 65p per tin.
● Bread – 80p per loaf.
● Milk – £1.30 per bottle.
● Apples – £1.00 per bag.
Current special offers are as follows:
● Apples have a 10% discount off their normal price this week.
● Buy 2 tins of soup and get a loaf of bread for half price.
Please write a program that accepts a list of products into a shopping basket and then outputs the
subtotal, as well as the special offer discounts and the final price.
Input should be via the command line in the form: PriceBasket product1 product2 product3
For example: PriceBasket Apples Milk Bread
Output should be to the console, for example:
Subtotal: £3.10
Apples 10% off: 10p
Total: £3.00
If no special offers are applicable the code should output:
Subtotal: £1.30 (No offers available)
Total price: £1.30
