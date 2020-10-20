# Write a function called 'PrintBoxByWidth' that prints out a box that looks like below, at the specified width. DO
# NOT add or edit any print statements in the code provided; you may only move them around your code.
# PrintBoxByWidth(60) =>
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# x                                                          x
# xoooooooooooooooooooooooooooooooooooooooooooooooooooooooooox
# x                                                          x
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# 
# print("x", end='')
# print("o", end='')
# print(" ", end='')
# print("")


def PrintBoxByWidth(width):

    for i in range (0,width):
        print('x', end = '')
    print()

    for i in range (0,width):
        if i == 0 or i == (width-1):
            print ('x', end = '')
        else:
            print (' ', end = '')
    print()

    for i in range (0,width):
        if i == 0 or i == (width-1):
            print ('x', end = '')
        else:
            print ('o', end = '')
    print()

    for i in range (0,width):
        if i == 0 or i == (width-1):
            print ('x', end = '')
        else:
            print (' ', end = '')
    print()

    for i in range (0,width):
        print('x', end = '')
    print()

PrintBoxByWidth(95)