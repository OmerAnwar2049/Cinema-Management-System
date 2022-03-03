# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 19:13:10 2020

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


# Individual account
class Account:
    def __init__(self,name,email,psw):
        self.name = name
        self.email = email
        self.psw = psw
        self.due_tickets = []
        self.saved_tickets = []
        self.is_member = False
        self.acc_membership = None

    def DisplayAccount(self):
        print(self.name + " " + self.email+ " "+ self.psw)
        

    # Storing booked tickets here
    def addTicket(self, ticket):
        self.due_tickets.append(ticket)
        

    # Paying dues for booked tickets
    def payDues(self,method,bank_acc):
        self.saved_tickets += self.due_tickets
        self.due_tickets.clear()
        if ServiceFactory().getInstance().getPaymentHandler(method).payDues(bank_acc) == "yes":
            return self.saved_tickets
        
    # Upgrading to member account
    def upgradeToMember(self):
        if self.is_member == False:
            self.acc_membership = Membership()
            self.is_member = True
            return "yes"
        else:
            return "no"
        
    # Payment for upgrading to member account
    def registerPayment(self,method,bank_acc):
        return ServiceFactory().getInstance().getPaymentHandler(method).payDues(bank_acc)
        
    # For getting membeship charges
    def getMemberDues(self):
        return self.acc_membership.getDues()
    
    # paying membership charges
    def payMemberDues(self, method,bank_acc):     
        check = ServiceFactory().getInstance().getPaymentHandler(method).payDues(bank_acc)
        if check == "yes":
            self.acc_membership.member_dues = 0
            self.acc_membership.remaining_days += 30
        return "yes"
    
    #Refund Ticket
    #1) Removes ticket form stored ticket list
    #2) Adds movie credit to user momber account
    
    def addRefundMoney(self,ticket):
        for i in range(len(self.saved_tickets)):
            if self.saved_tickets[i].show.movie.name == ticket.show.movie.name:
                if self.saved_tickets[i].show.time_slot == ticket.show.time_slot:
                    if self.saved_tickets[i].show.hall.hall_no == ticket.show.hall.hall_no:
                        if self.saved_tickets[i].seat.seat_no == ticket.show.seat.seat_no:
                            self.saved_tickets.pop(i)
                            break
        self.acc_membership.refunded_money+=500



