#################################################################
# File name: ex007                                              #
# Author: Leonardo Almeida                                      #
# GitHub: leo_nardow                                            #
#################################################################
# Subject: Treating data and doing the math                     #
# Description: Make a program that reads two grade of a student,#
# calculates and shows its average                              #
#################################################################

name = input("Type the student's name: ")
g1 = float(input('Type the first grade: '))
g2 = float(input('Type the second grade: '))

g1 = (g1+g2)/2

print("{}'s average is {:.1f}".format(name, g1))
