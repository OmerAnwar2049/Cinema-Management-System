# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 22:08:51 2020

@author: Omer
"""
import pickle

from classes import *


#Seat Save
"""
def saveAccount(seats):
    with open('Seats.pkl', 'wb') as output:
        pickle.dump(seats, output, pickle.HIGHEST_PROTOCOL)
        print("Successfully saved to pickle file")
seats = []
seats.append(Seat("1"))
seats.append(Seat("2"))
seats.append(Seat("3"))
seats.append(Seat("4"))
seats.append(Seat("5"))
seats.append(Seat("6"))
seats.append(Seat("7"))
seats.append(Seat("8"))
seats.append(Seat("9"))
seats.append(Seat("10"))
saveAccount(seats)
"""

"""
#Accounts save
def saveAccount(accounts):
    with open('Accounts.pkl', 'wb') as output:
        pickle.dump(accounts, output, pickle.HIGHEST_PROTOCOL)
        print("Successfully saved to pickle file")
        
a = []
a.append(Account("omer","foo@foolish.com","1234"))
a.append(Account("ali","foo@foolish.com","1234"))
a.append(Account("buraq","foo@foolish.com","12345"))
saveAccount(a)
"""   

#Movies save
"""
def saveAccount(seats):
    with open('UpcomingMovies.pkl', 'wb') as output:
        pickle.dump(seats, output, pickle.HIGHEST_PROTOCOL)
        print("Successfully saved to pickle file")
seats = []
seats.append(Movie("Predator 2019"))
seats.append(Movie("Terminator 4"))
seats.append(Movie("Dil Wale Dulhaniya le jayen Ge"))
seats.append(Movie("Cindrella"))
seats.append(Movie("12 Years a slave"))
saveAccount(seats)

for i in range(len(seats)):
    seats[i].displayMovie()
"""


# Shows save
"""
m1 =Movie("James Bond")
m2 =Movie("Maze Runner")
m3 =Movie("Hades")
m4 =Movie("Wrath of the titans")

h1 = Hall("1")
h2 = Hall("1")
h3 = Hall("1")
h4 = Hall("1")

def saveAccount(seats):
    with open('CurrentShows.pkl', 'wb') as output:
        pickle.dump(seats, output, pickle.HIGHEST_PROTOCOL)
        print("Successfully saved to pickle file")
L = []
L.append(Show("9:30-11:00",m1,h1))
L.append(Show("12:00-2:00",m2,h2))
L.append(Show("4:00-6:00",m3,h3))
L.append(Show("7:00-9:00",m4,h4))
saveAccount(L)

#for i in range(len(L)):
    #L[i].displayShow()

with open('CurrentShows.pkl', 'rb') as input:
    read_data = pickle.load(input)    
    
for i in range(len(read_data)):
    read_data[i].displayShow()
"""






