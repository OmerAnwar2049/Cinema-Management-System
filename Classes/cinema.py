from abc import ABC, abstractmethod
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
from showtimes import Showtimes
from users import Users
from booking import Booking

# Cinema class [Controller]
class Cinema:
    
    # Constructor
    def __init__(self):
        self.show_times = None
        self.hall_1 = Hall(1)
        self.hall_2 = Hall(2)        
        self.users = Users()
        self.booking = None
        self.user_acc = None #session
        self.upcoming_movies = None

    # Login Function for customer
    def Login(self, name, psw):
        self.user_acc = self.users.getAcc(name,psw)
        if self.user_acc != None:
            return "yes" 
        else:
            return "no"
            
    # Returns List of upcoming movies
    def browseMovies(self):
        self.upcoming_movies = ServiceFactory().getInstance().getPersistentHandler().loadUpcomingList()
        return self.upcoming_movies
    
    # Create Account
    def createAccount(self, name, email, psw):
       verify = self.users.getAcc(name,psw)       
       if verify == None:      
           self.users.CreateAccount(name, email, psw)
           return "yes"
       else:
           return "no"
       
        
    # Update Account
    def updateAccount(self,name,email,psw):
        verify =  self.users.updateAccount(name,email,psw,self.user_acc)
        
        if(verify == "yes"):
            self.user_acc.name=name
            self.user_acc.email = email
            self.user_acc.psw = psw
            return "yes"
        else:
            return "no"

    # Delete Account
    def deleteAccount(self):
        return self.users.deleteAccount(self.user_acc)
        
    
    # Book Ticket starts here      
    def intitaiteBooking(self):
        self.show_times = Showtimes()
        self.booking = Booking(self.user_acc)
        self.current_shows = self.show_times.getCurrentShows()
        return self.current_shows

    def selectShow(self, movie, time): 
        show = self.show_times.selectShow(movie, time)      
        self.booking.setShow(show)
        self.available_seats = show.getAvailableSeats()
        return self.available_seats

    def selectSeat(self, seat_num):
        dues = self.booking.selectSeat(seat_num)
        self.show_times.updateShowSeats(self.booking.show)
        return dues  
        
    def payDues(self, method, bank_acc):
        user_tickets = self.booking.payDues(method, bank_acc)
        self.user_acc.saved_tickets = user_tickets
        self.users.save(self.user_acc)       
        return user_tickets
        
        
    
    # Upgrade To Member Account
    def upgradeToMember(self,method,bank_acc):
        check1 = self.user_acc.upgradeToMember()
        if check1 == "yes":
            self.users.updateMemberAccount(self.user_acc)
            return self.user_acc.registerPayment(method,bank_acc)           
        else:
            return "no"
            
    # Pay Member Dues
    def initiateMemberDues(self):
        if self.user_acc.is_member == True:
            return self.user_acc.getMemberDues()
        else:
            return -1
    
    def payMemberDues(self, method, bank_acc):
        return self.user_acc.payMemberDues(method,bank_acc)
    
    
    # RefundTickets   
    def initiateRefundTicket(self):
        return self.user_acc.save_tickets
    
    def refundTicket(self,ticket):
        self.show_times.refundTicket(ticket)
        self.user_acc.addRefundMoney(ticket)
        self.users.save(self.user_acc)
        

