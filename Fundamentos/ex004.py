#################################################################
# File name: ex004                                              #
# Author: Leonardo Almeida                                      #
# GitHub: leo_nardow                                            #
#################################################################
# Subject: Treating data and doing the math                     #
# Description: Make a program that reads something from the     #
# keyboard and displays its primitive type and all possible     #
# information about it on the screen.                           #
#################################################################

n = input('Type anything: ')
print('The primitive type is: ', type(n))
print('Is it made only by spaces? ', n.isspace())
print('Is it numeric? ', n.isnumeric())
print('Is it alpha?', n.isalpha())
print('Is it alphanumeric? ', n.isalnum())
print('Is it in UpperCase? ', n.isupper())
print('Is it in LowerCase? ', n.islower())
print('Is it capitalized? ', n.istitle())
print('Capitalized version: ', n.capitalize())
