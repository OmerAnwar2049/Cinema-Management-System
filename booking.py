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


class Booking:
    def __init__(self,user_acc):
        self.user_account = user_acc
        self.show = None
        self.due_ammount = 0

    # Setting account in the booking
    def setAccount(self, user):
        self.user_account = user

    # Setting Show
    def setShow(self, show):
        self.show = show  
    
    # Book one seat
    def selectSeat(self, seat_num):
        seat = self.show.getSeat(seat_num)
        ticket = Ticket(self.show, seat)
        self.user_account.addTicket(ticket)
        self.due_ammount += 500
        
        #In case of member check for refund
        if self.user_account.is_member == True:
            if self.user_account.acc_membership.refunded_money != 0:
                self.due_ammount = self.due_ammount - self.user_account.acc_membership.getRefundMoney()
                self.user_account.acc_membership.refunded_money-500
        return self.due_ammount

    #Pay dues for booked tickets
    def payDues(self, method, bank_acc):
        return self.user_account.payDues(method, bank_acc)