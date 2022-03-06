# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 19:09:44 2020

@author: Omer
"""


#Membership class
class Membership:
    def __init__(self):
        self.member_dues = 500
        self.remaining_days = 30
        self.refunded_money = 0
        
    def getDues(self):
        return self.member_dues
    
    def getRefundMoney(self):
        return self.refunded_money