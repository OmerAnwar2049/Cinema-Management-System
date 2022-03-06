# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 19:19:10 2020

@author: Omer
"""

import pickle
import os
from movie import Movie
from seat import Seat
from membership import Membership
from hall import Hall
from ticket import Ticket
from servicefactory import ServiceFactory
from show import Show
from account import Account
from showtimes import Showtimes

# Contains all the user's accounts
class Users:
    def __init__(self):
        self.accounts = []
        self.accounts = ServiceFactory().getInstance().getPersistentHandler().loadAccountList()       
        
    def CreateAccount(self,name,email,psw):
        acc = Account(name,email,psw)
        self.accounts.append(acc)
        self.save()
        
    def updateAccount(self,name,email,psw,user_acc):
        for i in range(len(self.accounts)):
            if self.accounts[i].name == user_acc.name:
                if self.accounts[i].psw == user_acc.psw:
                    self.accounts[i].name = name
                    self.accounts[i].email = email
                    self.accounts[i].psw = psw
                    break
        ServiceFactory().getInstance().getPersistentHandler().saveAccount(self.accounts)
        return "yes"
    
    def deleteAccount(self,user_acc):
        for i in range(len(self.accounts)):
            if self.accounts[i].name == user_acc.name:
                if self.accounts[i].psw == user_acc.psw:
                    self.accounts.pop(i)                  
                    break
        ServiceFactory().getInstance().getPersistentHandler().saveAccount(self.accounts)
        return "yes"
        
    def DisplayAccounts(self):
        for i in range(len(self.accounts)):
            print(self.accounts[i].DisplayAccount())
            
                
    def save(self,user_acc): 
        for i in range(len(self.accounts)):
            if self.accounts[i].name == user_acc.name:
                if self.accounts[i].psw == user_acc.psw:
                    self.accounts[i].saved_tickets = user_acc.saved_tickets
        ServiceFactory().getInstance().getPersistentHandler().saveAccount(self.accounts)   
    
    # Finding specific stored account from stored list
    def findAcc(self, name, psw):
        for i in range(len(self.accounts)):
            if self.accounts[i].name == name:
                if self.accounts[i].psw == psw:
                    return i
        return -1
    
    # Returning specific stored account from stored list
    def getAcc(self, name, psw):
        num = self.findAcc(name, psw)
        if(num != -1):
            return self.accounts[num] 
        else:
            return None
    
    #updating a previous free account user to member account and storing to database
    def updateMemberAccount(self,user_acc):
        for i in range(len(self.accounts)):
            if self.accounts[i].name == user_acc.name:
                if self.accounts[i].psw == user_acc.psw:
                    self.accounts[i] = user_acc
                    break
        ServiceFactory().getInstance().getPersistentHandler().saveAccount(self.accounts)