#################################################################
# File name: ex010                                              #
# Author: Leonardo Almeida                                      #
# GitHub: leo_nardow                                            #
#################################################################
# Subject: Treating data and doing the math                     #
# Description: Make a program that reads how many reais a person#
# has in their wallet and shows how many dollars they can buy   #
# Consider: U$1,00 = R$5,25                                     #
#################################################################

money = float(input('Type the amount you want to convert: R$'))

print('With this amount you cant buy U${:.2f}'.format(money/5.25))
