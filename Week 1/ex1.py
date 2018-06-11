# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 14:00:28 2018

@author: Rik
"""

deposit = float(input("Deposit amount: "))
rate = float(input("Interest rate: "))/100

bal = deposit
year = 1
while year <= 3:
    bal = bal + rate*bal
    year += 1

print("Your balance after 3 years is $", format(bal, '.2f'))
