#################################################################
# File name: ex006                                              #
# Author: Leonardo Almeida                                      #
# GitHub: leo_nardow                                            #
#################################################################
# Subject: Treating data and doing the math                     #
# Description: Create a program that reads a number and displays#
# its double, triple and square root                            #
#################################################################

n = int(input('Type a number: '))

print('The double is {}\nThe triple is {}\nThe square root is {}'.format(n * 2, n * 3, n ** (1 / 2)))
