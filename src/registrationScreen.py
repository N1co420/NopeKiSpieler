# This File is the implementation of a screen for user registration
from tkinter import*
import requests
import json
 
# set global variables
 
global username
global password
global username_entry
global password_entry

def main_account_screen():
    global main_screen
    main_screen = Tk() # create the GUI window
    main_screen.geometry("300x250") # set the configuration of the GUI window
    main_screen.title("Accoount Login") # set the title of the GUI window

    # create a form label
    Label(text="Choose Login Or Register", bg="blue", width="300", height="2").pack()
    Label(text="").pack()

    # create a login Button
    Button(text="login", height="2", width="30", command=login).pack()
    Label(text="").pack()

    # create a reigster Button
    Button(text="Register", height="2", width="30", command=register).pack()
    Label(text="").pack()

def register():
    global username
    global password
    global username_entry
    global password_entry

    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("300x300")

    # set text variables
    username = StringVar()
    password = StringVar()
    firstname = StringVar()
    lastname = StringVar()

    # set username label and entry
    Label(register_screen, text="Please enter details below", bg="blue").pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="username")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()

    # set password label and entry
    password_lable = Label(register_screen, text="password * ")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()

    # set password label and entry
    firstname_lable = Label(register_screen, text="firstname  ")
    firstname_lable.pack()
    firstname_entry = Entry(register_screen, textvariable=firstname)
    firstname_entry.pack()

    # set password label and entry
    lastname_lable = Label(register_screen, text="lastname  ")
    lastname_lable.pack()
    lastname_entry = Entry(register_screen, textvariable=lastname, show='*')
    lastname_entry.pack()

    Label(register_screen, text="").pack()

    # set register button
    Button(register_screen, text="Register", width=10, height=1, bg="blue", command = register_user).pack()

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
   
    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password__login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password__login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command=login_verification).pack()
   
def login_verification():
   print("test")
    

def register_user():
    print("test")

def main():
    
    main_account_screen()

    main_screen.mainloop()


    
main()


