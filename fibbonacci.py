# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 00:09:10 2020

@author: raman
"""

a = 0
b = 1
while a < 10:
    print(a)
    a, b = b, a + b
print(a, b)    