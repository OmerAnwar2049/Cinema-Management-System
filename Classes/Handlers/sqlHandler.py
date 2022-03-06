import pickle
import os
from perHandler import PersistentHandler


# Sql handling class
class MySqlHandler(PersistentHandler):
    def saveAccount(self, account):
        #implementation of saving to a file here
        print(account.name + " saved to file")