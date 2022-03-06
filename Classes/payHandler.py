from abc import ABC, abstractmethod
import pickle
import os
# Abstract class for payment
class PaymentHandler(ABC):
    @abstractmethod
    def payDues(self):pass

