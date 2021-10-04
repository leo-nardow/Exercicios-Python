#################################################################
# File name: ex012                                              #
# Author: Leonardo Almeida                                      #
# GitHub: leo_nardow                                            #
#################################################################
# Subject: Treating data and doing the math                     #
# Description: Make a program that reads the price of a product #
# and shows its new price, with 5% off                          #
#################################################################

price = float(input("Type the product's price: "))

price = price * 0.95

print('The new price is {}'.format(price))
