#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 31 23:48:27 2024

@author: charleshuang
"""

#Launch School

# You may modify this line
#Making deep copies

import copy

dict1 = {
    'a': [[7, 1], ['aa', 'aaa']],
    'b': ([3, 2], ['bb', 'bbb']),
}

dict2 = copy.deepcopy(dict1)

# All of these should print False
print(dict1         is dict2)
print(dict1['a']    is dict2['a'])
print(dict1['a'][0] is dict2['a'][0])
print(dict1['a'][1] is dict2['a'][1])
print(dict1['b']    is dict2['b'])
print(dict1['b'][0] is dict2['b'][0])
print(dict1['b'][1] is dict2['b'][1])


#####

#Make a shallow copy without using the copy module

dict1 = {
    'a': [{7, 1}, ['aa', 'aaa']],
    'b': ({3, 2}, ['bb', 'bbb']),
}

dict2 = dict(dict1)

print(dict1         is dict2)
print(dict1['a']    is dict2['a'])
print(dict1['a'][0] is dict2['a'][0])
print(dict1['a'][1] is dict2['a'][1])
print(dict1['b']    is dict2['b'])
print(dict1['b'][0] is dict2['b'][0])
print(dict1['b'][1] is dict2['b'][1])

###

def do_something(dictionary):
    return sorted(dictionary.keys())[1].upper()

#Defines a f. that takes a dict, then returns the capitalized second value of the dictionary keys sorted in ascending order. So it should return CHRIS.

my_dict = {
    'Karl':     108,
    'Clare':    175,
    'Karis':    140,
    'Trevor':   180,
    'Antonina': 132,
    'Chris':    101,
}

print(do_something(my_dict))

import math
import math as asdfghjkl
from math import sqrt

print(sqrt(37))
print(math.sqrt(37))
print(asdfghjkl.sqrt(37))

def sum_of_squares(num1, num2):
    
    #Need a nested function here to define square
    def square(n):
        return n ** 2

    return square(num1) + square(num2)

print(sum_of_squares(3, 4))   # 25 (3 * 3 + 4 * 4)
print(sum_of_squares(5, 12))  # 169 (5 * 5 + 12 * 12)

####

counter = 0

def increment_counter():
    counter += 1
    return counter

print(counter)                # 0

increment_counter()
print(counter)                # 1

increment_counter()
print(counter)                # 2

counter = 100
increment_counter()
print(counter)                # 101

###

counter = 0

def increment_counter():
    counter += 1
    return counter

print(counter)       

###

test = 4


def add_test(x):
    test += 1
    return x + test

print(add_test(10))
