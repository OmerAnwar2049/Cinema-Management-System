import pickle
import os
from payHandler import PaymentHandler

#For debit payment method 
class DebitHandler(PaymentHandler):
    def payDues(self, account):
        print("Debit Transaction from "+ account)
        return "yes"