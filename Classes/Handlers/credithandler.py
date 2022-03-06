import pickle
import os
from payHandler import PaymentHandler

#For handling credit Card payment method
class CreditHandler(PaymentHandler):
    def payDues(self, account):
        print("Credit Transaction from "+ account)
        return "yes"