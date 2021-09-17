#################################################################
# File name: ex008                                              #
# Author: Leonardo Almeida                                      #
# GitHub: leo_nardow                                            #
#################################################################
# Subject: Treating data and doing the math                     #
# Description: Make a program that reads a value in meters and  #
# displays it converted to centimeters and millimeters          #
#################################################################

d = float(input('Type the distance: '))

print('{}m corresponds to :'.format(d))
print('{}km'.format(d/1000))
print('{}hm'.format(d/100))
print('{}dam'.format(d/10))
print('{}dm'.format(d*10))
print('{}cm'.format(d*100))
print('{}mm'.format(d*1000))
