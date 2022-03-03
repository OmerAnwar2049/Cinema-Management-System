# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 19:17:39 2020

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

# Showtimes / Movie catalogue
class Showtimes:
    def __init__(self):
        self.currentShows = ServiceFactory().getInstance().getPersistentHandler().loadCurrentShows()

    
    def display(self):
        for i in range(len(self.currentShows)):
            print("Show: "+ self.currentShows[i].movie.name+", Time: "+ self.currentShows[i].time_slot)
            
    # reurning current shows for book ticket
    def getCurrentShows(self):
        return self.currentShows

    #updating showlist after seat booking and storing it to data base
    def updateShowSeats(self,show):
        for i in range(len(self.currentShows)):
            if show.movie.name == self.currentShows[i].movie.name:
                self.currentShows[i].availableSeats = show.availableSeats
                break
             
        ServiceFactory().getInstance().getPersistentHandler().saveCurrentShows(self.currentShows)
 
    #reutrning one specific show in book ticket use case
    def selectShow(self, movie, time):
        num = -1
        for i in range(len(self.currentShows)):
            if self.currentShows[i].movie.name == movie and self.currentShows[i].time_slot == time:
                num = i
                break
        return self.currentShows[num]

    def displayCurrentShows(self):
        for i in range(len(self.currentShows)):
            self.currentShows[i].displayShow()
            
    #Refund ticket operation in shows list and storing to databsae
    def refundTicket(self,ticket):
        for i in range(len(self.currentShows)):
            if(self.currentShows[i].show.movie.name == ticket.show.movie.name):
                if(self.currentShows[i].show.time_slot == ticket.show.time_slot):
                    if(self.currentShows[i].show.hall.hall_no == ticket.show.hall.hall_no):
                        self.currentShows[i].freeSeat(ticket.seat.seat_no)
                        break
        ServiceFactory().getInstance().getPersistentHandler().saveCurrentShows(self.currentShows)
        return "yes"