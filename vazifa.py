#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 10:22:24 2023

@author: saidakbar
"""
num1 = int(input('Please enter number'))
vari = str(input(f'please enter variable : ')) 
num2 = int(input('Please enter your seconda number'))
if vari == '+':
      print(num1 + num2)
elif vari == '/':
    print(num1 // num2)
elif vari == '-':
    print(num1 - num2)
elif vari == '*':
    print(num1 * num2)        
else :
    print('what a fucking you doing I said you to enter number ')