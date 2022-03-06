from abc import ABC, abstractmethod
import pickle
import os
# Abstract Class for DBHandler
class PersistentHandler(ABC):
    @abstractmethod
    def saveAccount(self):pass
    def loadAccountList(self):pass
