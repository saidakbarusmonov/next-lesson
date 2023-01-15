#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 01:53:32 2023

@author: saidakbar
"""
#Tip Calculator
foodAmount = int(input(f'Please enter your food amount:  '))
print(foodAmount)
tipAmount = int(input(f'Please enter your tip amount'))
print(tipAmount)
tipcal = tipAmount * 0.01
def total(a, b):
    return a + b
print(total(foodAmount, tipAmount))
total()
