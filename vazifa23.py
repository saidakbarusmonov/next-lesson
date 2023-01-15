#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 12:52:35 2023

@author: saidakbar
"""

command = ''
while command != 'quit':
    command = input('>>> ').lower()
    if command == 'help':
        print('''[start] - to start the game
              [stop] - to stop the car
              [quit] - to exit
              ''')
    elif command == 'start':
        print('car is being runned')
    elif command =='quit':
        print('byeee')
    elif command == 'stop':
        print('your car has been stopped')
    else:
        print('i didnt understand that')