#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 18:07:38 2024

@author: charleshuang
"""

#Easy Part 1

#1/11
#Write a function that takes one integer argument and returns True when the number's absolute value is odd, False otherwise.

def is_odd(int):
    return True if int % 2 == 1 else False

is_odd(23483)   
is_odd(38746)

#2/11
#Print all odd numbers from 1 to 99, inclusive, with each number on a separate line.
for i in range(1, 100):
    if i % 2 == 1:
        print(i)

#How to iterate over only the odd numbers:
for i in range(1, 100, 2):
    print (i)

#3/11
