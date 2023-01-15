#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 05:52:40 2023

@author: saidakbar
"""
# project: Weight converter
client_weight = float(input('Please enter your weight: '))
client_weight_check = input('choose weight type K(kilogramm) or P(pound)')
cal_weight_pound = client_weight / 0.454
cal_weight_kilogram = client_weight * 0.454
if client_weight_check == 'kg':
    print(cal_weight_pound)
elif client_weight_check == 'p':
    print(cal_weight_kilogram)
else:
    print('you didnt enter true weight amount ')