import pickle
import os
from perHandler import PersistentHandler

# Oracle DB Class
class OracleHandler(PersistentHandler):
    def saveAccount(self, account):
         #implementation of Oracle db here
         print(account.name + " saved to oracle database")