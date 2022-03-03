import pickle
import os
from hall import *
from perHandler import PersistentHandler

# Pickle used primaril;y for this project,stores entire objects or list of objects in pkl files
class PickleHandler(PersistentHandler):
    
    # For saving accounts
    def saveAccount(self, accounts):
        with open('Accounts.pkl', 'wb') as output:
            pickle.dump(accounts, output, pickle.HIGHEST_PROTOCOL)
            print("Successfully saved to pickle file")
        
    # Loading Account List on startup
    def loadAccountList(self):
        read_data = []
        if os.path.getsize('Accounts.pkl') != 0:
            with open('Accounts.pkl', 'rb') as input:
                read_data = pickle.load(input)
        return read_data 
    
    # Load seat List 
    def loadSeatList(self):
        read_data = []
        if os.path.getsize('Seats.pkl') != 0:
            with open('Seats.pkl', 'rb') as input:
                read_data = pickle.load(input)
        return read_data   

    # Load upcoming list of movies,used in browse movies use case
    def loadUpcomingList(self):
        read_data = []
        if os.path.getsize('UpcomingMovies.pkl') != 0:
            with open('UpcomingMovies.pkl', 'rb') as input:
                read_data = pickle.load(input)
        return read_data    

    # Load list of shows in containes class of showtimes
    def loadCurrentShows(self):
        read_data = []
        if os.path.getsize('CurrentShows.pkl') != 0:
            with open('CurrentShows.pkl', 'rb') as input:
                read_data = pickle.load(input)
        return read_data
    
    # Savinf updated shows list
    def saveCurrentShows(self,cur_shows):       
        with open('CurrentShows.pkl', 'wb') as output:
            pickle.dump(cur_shows, output, pickle.HIGHEST_PROTOCOL)
            print("Successfully saved to pickle file")   
            
            
    def loadBookedTickets(self):
        read_data = {}
        if os.path.getsize('TicketDictionary.pkl') != 0:
            with open('TicketDictionary.pkl', 'rb') as input:
                read_data = pickle.load(input)
        return read_data

    def saveTickets(self, booked_tickets):
        with open('TicketDictionary.pkl', 'wb') as output:
            pickle.dump(booked_tickets, output, pickle.HIGHEST_PROTOCOL)
            print("Saved to pickle file")