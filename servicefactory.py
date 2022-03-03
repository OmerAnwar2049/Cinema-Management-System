import pickle
import os
from picklehandler import PickleHandler
from oracleHandler import OracleHandler
from sqlHandler import MySqlHandler
from credithandler import CreditHandler
from debithandler import DebitHandler

#Factory and handlers
class ServiceFactory():
    
    service_factory = None  #Static instance of Service Factory
    
    #Constructor
    def __init__(self):
        self.pers_handler = None
        self.payment_handler = None
        
        
        f = open("database.txt","r")
        if f.mode == "r":
            self.save_type = f.read()  #Database type is put here
            
    
    # For setting Data Base type
    def getPersistentHandler(self):
        if self.pers_handler == None:
            if self.save_type ==  "pickle":
                self.pers_handler = PickleHandler()
            elif self.save_type == "mysql":
                self.pers_handler = MySqlHandler()
            elif self.save_type == "oracle":
                self.pers_handler = OracleHandler()
        return self.pers_handler


    # For setting Payment Type
    def getPaymentHandler(self,method):
        if self.payment_handler == None:
            if method ==  "credit":
                self.payment_handler = CreditHandler()
            elif method == "debit":
                self.payment_handler = DebitHandler()
        return self.payment_handler

    # Static Function
    @staticmethod
    def getInstance():  #Static method to get the instance of Service Factory
        if ServiceFactory.service_factory == None:
            ServiceFactory.service_factory = ServiceFactory()
        return ServiceFactory.service_factory
    


