import pickle
import os
from movie import Movie
from seat import Seat
from servicefactory import ServiceFactory

# Class for Halls
class Hall:
    def __init__(self,hallnum):
        self.hall_no = hallnum
        self.seats = ServiceFactory().getInstance().getPersistentHandler().loadSeatList()
        self.capacity = len(self.seats)

    def displaySeatList(self):
        for i in range(len(self.seats)):
            self.seats[i].displaySeat()
        print(self.capacity)


