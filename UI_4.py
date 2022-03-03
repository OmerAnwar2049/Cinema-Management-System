# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 12:01:44 2020

@author: Omer
"""

#import modules
 
from tkinter import *

import os

from classes import *

cinema = Cinema()
 
# Designing window for registration
 
def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("400x400")
 
    global username
    global password
    global email
    global username_entry
    global password_entry
    global email_entry
    username = StringVar()
    password = StringVar()
    email=StringVar()
 
    Label(register_screen, text="Please enter details below", bg="blue",foreground="white").pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Username * ")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(register_screen, text="Password * ")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    email_label = Label(register_screen, text="Email * ")
    email_label.pack()
    email_entry = Entry(register_screen, textvariable=email)
    email_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, bg="blue", foreground="white",command = register_user).pack()
 
 
# Designing window for login 
 
def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()
 
    global username_verify
    global password_verify
 
    username_verify = StringVar()
    password_verify = StringVar()
 
    global username_login_entry
    global password_login_entry
 
    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*') #to hide password 
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command = login_verify).pack()
 
# Implementing event on register button
 
def register_user():
 
    username_info = username.get()
    password_info = password.get()
    email_info = email.get()
 
    username_entry.delete(0, END)
    password_entry.delete(0, END)
    email_entry.delete(0, END)
    
    #print(username_info+" "+password_info+" "+email_info)
    check = cinema.createAccount(username_info,email_info,password_info)
 
    if check == "yes":
        Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()
    else:
        Label(register_screen, text="Registration Failed", fg="red", font=("calibri", 11)).pack()
        Label(register_screen, text="User already present :(", fg="red", font=("calibri", 11)).pack()
 
# Implementing event on login button 
 
def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)
    
    #Login Call to cinema
    check = cinema.Login(username1,password1)
    
    if check == "yes":
        login_sucess()
 
    else:
        user_not_found()
 
# Designing popup for login success
 
def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK", command=login_access).pack()


# when user log-in is cussessful
def login_access():
    login_success_screen.destroy()
    login_screen.destroy() 
    global use_cases_screen
    use_cases_screen=Toplevel(main_screen)
    use_cases_screen.title("USE-CASES")
    use_cases_screen.geometry("400x400")
    Label(use_cases_screen,text="").pack()
    Button(use_cases_screen,text="Update Account",bg="white",foreground="blue", font=("Calibri", 13,'bold'),height="2", width="30",activebackground='red',command=update_account).pack()
    Button(use_cases_screen,text="Book-Ticket",bg="white",foreground="blue", font=("Calibri", 13,'bold'),height="2", width="30",activebackground='red',command=Book_Ticket).pack()
   # Button(use_cases_screen,text="Pay_Membership_Dues",bg="white",foreground="blue", font=("Calibri", 13,'bold'),height="2", width="30",activebackground='red',commaand=pay_due_membership).pack()
    Button(use_cases_screen,text="Pay Membership Dues",bg="white",foreground="blue", font=("Calibri", 13,'bold'),height="2", width="30",activebackground='red',command=pay_due_membership).pack()
    Button(use_cases_screen,text="Upgrade Account",bg="white",foreground="blue", font=("Calibri", 13,'bold'),height="2", width="30",activebackground='red',command=upgrade_account).pack()
    Button(use_cases_screen,text="Delete Account",bg="white",foreground="blue", font=("Calibri", 13,'bold'),height="2", width="30",activebackground='red',command=Delete_Account_Success).pack()
    Button(use_cases_screen,text="EXIT",bg="black",foreground="red", font=("Calibri", 13,'bold'),height="2", width="30",activebackground='red',command=delete_login_success).pack()


# Designing popup for login invalid password
 
def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()
 
# Designing popup for user not found
 
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()
 
# Deleting popups


def delete_login_success():
    login_success_screen.destroy()
    login_screen.destroy() # close log-in window as well 
    use_cases_screen.destroy() # close the use case screen when exit is pressed
 
 
def delete_password_not_recognised():
    password_not_recog_screen.destroy()
 
 
def delete_user_not_found_screen():
    user_not_found_screen.destroy()
 
############################################### BOOK TICKEt ##############################################
def Book_Ticket():
    global Book_ticket_screen
    global list_shows
    global movie_enter
    global timing_enter
    global store_movie
    global store_timing
    list_shows= StringVar()
    store_movie=StringVar()
    store_timing=StringVar()

    list_shows= cinema.intitaiteBooking()#calling available shows
       
    Book_ticket_screen=Toplevel(main_screen)
    Book_ticket_screen.title("Select Movie to Watch")
    Book_ticket_screen.geometry("600x600")
    Label(Book_ticket_screen,text="").pack()
    
    Label(Book_ticket_screen,text="SELECT SHOW",font=("Calibri", 20,'bold')).pack()
    
    #Displaying shows
    for i in range(len(list_shows)):
        Label(Book_ticket_screen,text="").pack()
        Label(Book_ticket_screen,text=list_shows[i].movie.name).pack()
        Label(Book_ticket_screen,text=list_shows[i].time_slot).pack()
    
    
    Label(Book_ticket_screen,text="").pack()
    Label(Book_ticket_screen, text="Movie * ").pack()
    movie_enter = Entry(Book_ticket_screen, textvariable=store_movie)
    movie_enter.pack()
    Label(Book_ticket_screen,text="").pack()
    Label(Book_ticket_screen, text="Time-Slot * ").pack()
    timing_enter = Entry(Book_ticket_screen, textvariable=store_timing)
    timing_enter.pack()
    Label(Book_ticket_screen,text="").pack()
    Label(Book_ticket_screen,text="").pack()
    

    Button(Book_ticket_screen,text="Proceed to Booking",bg="white",foreground="blue", font=("Calibri", 13,'bold'),height="2", width="30",activebackground='red',command=proceed_to_booking).pack()

def proceed_to_booking():
    Book_ticket_screen.destroy()
    global seat_booking_screen
    global seats_enter
    global store_seat
    
    mov = store_movie.get()
    tim = store_timing.get()
     
    available = cinema.selectShow(mov,tim)
    
    
    store_seat=StringVar()
    seat_booking_screen=Toplevel(main_screen)
    seat_booking_screen.title("Book Seats")
    seat_booking_screen.geometry("500x500")
    Label(seat_booking_screen,text="").pack()
    
    # Displaying Available Seats
    Label(seat_booking_screen,text="AVAILABLE SEATS",font=("Calibri", 20,'bold')).pack()
    
    for i in range(len(available)):
        Label(seat_booking_screen,text=available[i].seat_no).pack()
    
    Label(seat_booking_screen,text="Enter seat#").pack()
    seats_enter = Entry(seat_booking_screen ,textvariable=store_seat)
    seats_enter.pack()
    Label(seat_booking_screen,text="").pack()
    Label(seat_booking_screen,text="").pack()
    Button(seat_booking_screen,text="Book Seat",bg="blue",foreground="white", font=("Calibri", 13,'bold'),height="2", width="15",activebackground='red',command = addSeat).pack() 
    #add_seat func here
    
    
   
    Label(seat_booking_screen,text="").pack()
    Button(seat_booking_screen,text="Proceed to Payment",bg="black",foreground="red", font=("Calibri", 13,'bold'),height="2", width="15",activebackground='red',command=proceed_to_payment).pack()
    seat_booking_screen.mainloop()

#def add_seat(): // add functionality to book seats for the user

def addSeat():
    S = store_seat.get()
    
    global save_bill
    save_bill = StringVar()
    save_bill = str(cinema.selectSeat(S))
    




def proceed_to_payment():
    seat_booking_screen.destroy()
    global payment_screen
    global card_enter
    global card_store
    global bill
    global payment_method
    payment_method=IntVar()
    bill=StringVar()
    bill = save_bill
    card_store=StringVar()
    
    payment_store=StringVar()
    payment_screen=Toplevel(main_screen)
    payment_screen.title("Pay Bill")
    payment_screen.geometry("400x400")
    Label(payment_screen,text="").pack()
    Label(payment_screen,text="Total bill is >> " + bill).pack()
    Label(payment_screen,text="").pack()
    Radiobutton(payment_screen, text="Credit", variable=payment_method,value=1).pack()
    Radiobutton(payment_screen, text="Debit",  variable=payment_method,value=2).pack()
    Label(payment_screen,text="").pack()
    Label(payment_screen,text="Please enter your card-Number").pack()
    card_enter = Entry(payment_screen ,textvariable=card_store)
    card_enter.pack()
    Label(payment_screen,text="").pack()
    Label(payment_screen,text="").pack()

    Button(payment_screen,text="Confirm Payment",bg="green",foreground="white", font=("Calibri", 13,'bold'),height="2", width="30",activebackground='red',command=payBooking).pack()


def payBooking():
    check = payment_method.get()
    if check == 1:
        choice = "credit"
    else:
        choice = "debit"
        
    cinema.payDues(choice,card_store.get())
    exit_payment_screen()

def exit_payment_screen():
    payment_screen.destroy()  

##########################################################################################################
## browse movies
def browse_movies():
    global brosw_movie_screen
    global movies
    #movies=StringVar()
    
    movies= cinema.browseMovies()
    
    brosw_movie_screen=Toplevel(main_screen)
    brosw_movie_screen.title("Browse Movies")
    brosw_movie_screen.geometry("500x500")
    Label(brosw_movie_screen,text="").pack()
    
    Label(brosw_movie_screen,text="UPCOMING MOVIES",font=("Calibri", 20,'bold')).pack()
    
    for i in range(len(movies)):
        Label(brosw_movie_screen,text="").pack()
        Label(brosw_movie_screen,text=movies[i].name).pack()
            
    Label(brosw_movie_screen,text="").pack()
    Label(brosw_movie_screen,text="").pack()
    Label(brosw_movie_screen,text="").pack()
    Button(brosw_movie_screen,text="CLOSE",bg="black",foreground="red", font=("Calibri", 13,'bold'),height="2", width="30",activebackground='red',command=exit_browse_movies).pack()

def exit_browse_movies():
    brosw_movie_screen.destroy()
################################################
## PAY-MEMBERSHIP-DUES 
def pay_due_membership():
    global pay_dues_Screen
    global card_enter1
    global card_store1
    global monthly_bill
    global payment_method1
    payment_method1=IntVar()
    monthly_bill=StringVar()
    card_store1=StringVar()
    monthly_bill="Your monthly member-ship bill is 50$"
    pay_dues_Screen=Toplevel(main_screen)
    pay_dues_Screen.title("Pay Membership Dues")
    pay_dues_Screen.geometry("400x400")
    Label(pay_dues_Screen,text="").pack()
    Label(pay_dues_Screen,text=monthly_bill).pack()
    Label(pay_dues_Screen,text="").pack()
    Radiobutton(pay_dues_Screen, text="Credit", variable=payment_method1,value=1).pack()
    Radiobutton(pay_dues_Screen, text="Debit",  variable=payment_method1,value=2).pack()
    Label(pay_dues_Screen,text="").pack()
    Label(pay_dues_Screen,text="Please enter your card-Number").pack()
    card_enter1 = Entry(pay_dues_Screen ,textvariable=card_store1)
    card_enter1.pack()
    Label(pay_dues_Screen,text="").pack()
    Label(pay_dues_Screen,text="").pack()

    Button(pay_dues_Screen,text="Confirm Payment",bg="green",foreground="white", font=("Calibri", 13,'bold'),height="2", width="30",activebackground='red',command=paid).pack()

def paid():
    check = payment_method1.get()
    if check == 1:
        choice = "credit"
    else:
        choice = "debit"
    print(cinema.payMemberDues(choice,card_store1.get()))
    pay_dues_Screen.destroy()

def exit_payment_member_screen():
    pay_dues_Screen.destroy()
    
    

#############################################################
## update account
def update_account():
    global update_account_screen
    global new_email_entry, new_email
    global new_password_entry,new_password
    global new_username_entry,new_username
    new_email=StringVar()
    new_password=StringVar()
    new_username=StringVar()

    update_account_screen=Toplevel(main_screen)
    update_account_screen.title("Update Account")
    update_account_screen.geometry("400x400")

    Label(update_account_screen, text="Please enter details below", bg="blue",foreground="white").pack()
    Label(update_account_screen, text="").pack()
    username_lable_new = Label(update_account_screen, text="New Username * ")
    username_lable_new.pack()
    new_username_entry = Entry(update_account_screen, textvariable=new_username)
    new_username_entry.pack()
    password_lable_new = Label(update_account_screen, text="New Password * ")
    password_lable_new.pack()
    new_password_entry = Entry(update_account_screen, textvariable=new_password, show='*')
    new_password_entry.pack()
    email_label_new = Label(update_account_screen, text="New Email * ")
    email_label_new.pack()
    new_email_entry = Entry(update_account_screen, textvariable=new_email)
    new_email_entry.pack()
    Label(update_account_screen, text="").pack()
     
    Button(update_account_screen, text="Update", width=10, height=1, bg="blue", foreground="white",command=update_data).pack() #update_data function here 



    

#############################################################

def update_data():
    n_user = new_username.get()
    n_email = new_email.get()
    n_psw = new_password.get()
    
    cinema.updateAccount(n_user,n_email,n_psw)
    
    
    
### upgrade account
def upgrade_account():
    global upgrade_account_screen
    global upgrade_bill
    global card_store_upgrade
    card_store_upgrade=StringVar()
    global payment_method_upgrade
    upgrade_bill=StringVar()
    payment_method_upgrade=IntVar()
    upgrade_bill="Your total Bill is 100$"          # store bill here 
    upgrade_account_screen=Toplevel(main_screen)
    upgrade_account_screen.title("Upgrade Account")
    upgrade_account_screen.geometry("400x400")


    Label(upgrade_account_screen,text="").pack()
    Label(upgrade_account_screen,text=upgrade_bill).pack()
    Label(upgrade_account_screen,text="").pack()

    Radiobutton(upgrade_account_screen, text="Credit", variable=payment_method_upgrade,value=1).pack()
    Radiobutton(upgrade_account_screen, text="Debit",  variable=payment_method_upgrade,value=2).pack()
    Label(upgrade_account_screen,text="").pack()
    Label(upgrade_account_screen,text="Please enter your card-Number").pack()
    card_enter = Entry(upgrade_account_screen ,textvariable=card_store_upgrade)
    card_enter.pack()
    Label(upgrade_account_screen,text="").pack()
    Label(upgrade_account_screen,text="").pack()

    Button(upgrade_account_screen,text="Confirm Payment",bg="green",foreground="white", font=("Calibri", 13,'bold'),height="2", width="30",activebackground='red',command = upgraded).pack() # upgrade_it func here 
    

def upgraded():
    
    check = payment_method_upgrade.get()
    if check == 1:
        choice = "credit"
    else:
        choice = "debit"
    
    print(cinema.upgradeToMember(choice,card_store_upgrade.get()))
    

# def upgrade_it():    add functionality to update user's account 
############################################################
###### Delete_Account
def Delete_Account_Success():  # add functionality of delete account here 
    global Delete_Account_Screen
    Delete_Account_Screen=Toplevel(main_screen)
    Delete_Account_Screen.title("Deleting Account")
    Delete_Account_Screen.geometry("200x200")
    Label(Delete_Account_Screen,text="").pack()
    Label(Delete_Account_Screen,text="ACCOUNT DELETION SUCCES").pack()
    Label(Delete_Account_Screen,text="").pack()
    Button(Delete_Account_Screen, text="OK",command = deleteData).pack()
    
def delete_delete_success_screen():
    Delete_Account_Screen.destroy()

############################################################

def deleteData():
    cinema.deleteAccount()   
    Delete_Account_Screen.destroy()
    use_cases_screen.destroy()
    

# Designing Main(first) window
def exit_main_screen():
    main_screen.destroy()

def Start_Up_Interface():

    global main_screen
    main_screen = Tk()
    main_screen.geometry("400x400")
    main_screen.title("CINE-GOLD")
  
    Label(text="Select Your Choice", bg="blue",foreground='white', width="400", height="2", font=("Calibri", 13,'bold')).pack()
    Label(text="").pack()
    Button(text="Login",bg="white",foreground="blue" ,font=("Calibri", 13,'bold'),height="2", width="30",activebackground='red', command = login).pack()
    Label(text="").pack()
    Button(text="Register",bg="white",foreground="blue", font=("Calibri", 13,'bold'),height="2", width="30",activebackground='red', command=register).pack()
    Label(text="").pack()
    Button(text="Browse Movies",bg="white",foreground="blue", font=("Calibri", 13,'bold'),height="2", width="30",activebackground='red', command=browse_movies).pack()
    Label(text="").pack()
    Button(main_screen,text="EXIT",bg="black",foreground="red", font=("Calibri", 13,'bold'),height="2", width="30",activebackground='red',command=exit_main_screen).pack()
    main_screen.mainloop()
 
 
Start_Up_Interface() #main function calling 