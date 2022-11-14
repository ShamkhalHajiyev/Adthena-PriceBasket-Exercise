
from ast import Try
from dis import disco
from email import message, message_from_binary_file
import numpy as np
import pandas as pd
#from Discount


class PriceBasket():
    print("Welcome to Shamkhal's market. I am selling Soup, Bread, Milk, Apples in my market. \n\
    Price of products are following: \n\
    ● Soup – £0.65 per tin. \n\
    ● Bread – £0.80 per loaf. \n\
    ● Milk – £1.30 per bottle. \n\
    ● Apples – £1.00 per bag. \n\
    This week we have following discounts: \n\
   ● Apples have a 10% discount off their normal price this week. \n\
   ● Buy 2 tins of soup and get a loaf of bread for half price. \n\
    ")
    
    def __init__(self):
        self.list_products_prices = {'soup' : 0.65, 'bread': 0.80, "milk": 1.30, 'apples': 1.00}
        self.products = input('Please enter names of products. \nNote: Please put space between products:\n').split(" ")

        for i in self.products:
            if i.lower() not in self.list_products_prices.keys():
                message = "{} is not in our product list".format(i)
                raise Exception(message)

        self.quantities = input('Please enter quantity of products same order with names. \nNote: Please put space between quantities and use only integer values:\n').split(" ")
        


        if len(self.products) != len(self.quantities):
            raise Exception("Length of products and amounts is not matching!")
        else:
            pass
        

        self.products_quantities = {}


        for i in range(len(self.products)):
            self.products_quantities[self.products[i].lower()] = int(self.quantities[i])
        
    


    def calculate_total_output(self):
        subtotal = sum([self.products_quantities[i.lower()]*self.list_products_prices[i.lower()] for i in self.products])
        discount_messages = []
        discounts = []

        ###Discount for Apple
        if 'apples' in self.products_quantities.keys():
            self.discount_apple = self.list_products_prices['apples'] * 0.10 * self.products_quantities['apples']
            self.list_products_prices['apples'] = self.list_products_prices['apples'] * 0.9
            message_discount1 = 'Apples 10% off: £0.10, £0.10*{0}=£{1}'.format(self.products_quantities['apples'], round(self.discount_apple,3))
            discount_messages.append(message_discount1)
            discounts.append(int(self.discount_apple))

        ###Discount for Bread
        if 'soup' in self.products_quantities and self.products_quantities['soup'] >= 2 and 'bread' in self.products_quantities:
            self.discount_bread = self.list_products_prices['bread'] * 0.5 * self.products_quantities['bread']
            self.list_products_prices['bread'] = self.list_products_prices['bread'] * 0.5
            message_discount2 = '2 tins of soup, bread price 50% off:, £0.40, £0.40*{0}=£{1}'.format(self.products_quantities['bread'], round(self.discount_bread,3))
            discount_messages.append(message_discount2)
            discounts.append(int(self.discount_bread))


        if len(discount_messages) == 0:
            return "Subtotal: £{0} (No offers available)\nTotal: £{0}".format(subtotal)
        else:
            return "Subtotal: £{0} \nDiscount(s): {1} \nTotal: £{2}".format(subtotal, discount_messages, subtotal-sum(discounts))
            


        
if __name__ == '__main__':
    price = PriceBasket()
    a = price.calculate_total_output()
    print(a)
