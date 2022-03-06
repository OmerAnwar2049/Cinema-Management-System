# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 19:13:48 2020

@author: Omer
"""
import pickle
import os
from movie import Movie
from seat import Seat
from hall import Hall

# An instance of a show
class Show:
    def __init__(self, ts, movie, hall): 
        self.time_slot = ts
        self.movie = movie # object of class Movie
        self.hall = hall # object of hall
        self.availableSeats = self.hall.seats

    # Sending availble seats in book ticket use case
    def getAvailableSeats(self):
        return self.availableSeats

    # Booking a specific seat
    def getSeat(self, num):
        for i in range(len(self.availableSeats)):
            if self.availableSeats[i].seat_no == num:
                temp = self.availableSeats[i]
                self.availableSeats.pop(i)                
                break
        return temp
    
    # Making a specific seat avialble for reuse after refund
    def freeSeat(self,seat_num):
        self.availableSeats.append(seat_num)
        
    def displayShow(self):
        print(self.time_slot +" " + self.movie.name+" " + self.hall.hall_no)
        for i in range(len(self.availableSeats)):
            self.availableSeats[i].displaySeat()