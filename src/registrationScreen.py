# This File is the implementation of a screen for user registration
from tkinter import*
import requests
import json
 
# set global variables
 
global username
global password
global username_entry
global password_entry

BASE_URL = "http://your-api-url.com"


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
    register_screen.geometry("300x250")

    # set text variables
    username = StringVar()
    password = StringVar()

    # set username label and entry
    Label(register_screen, text="Please enter details below", bg="blue").pack()
    Label(register_screen, text="").pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()

    # set password label and entry
    password_lable = Label(register_screen, text="Password * ")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()

    Label(register_screen, text="").pack()

    # set register button
    Button(register_screen, text="Register", width=10, height=1, bg="blue", command = register_user).pack()


def register_user():
    # get username and password
    username_info = username.get()
    password_info = password.get()

    # make a POST request to register a new user
    url = BASE_URL + "/register"
    payload = {"username": username_info, "password": password_info}
    response = requests.post(url, json=payload)

    if response.status_code == 200:
        # show success message on screen
        Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()
    else:
        # show error message on screen
        Label(register_screen, text="Registration Failed", fg="red", font=("calibri", 11)).pack()


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
    # get username and password
    username_info = username_verify.get()
    password_info = password_verify.get()

    # make a POST request to verify login credentials
    url = BASE_URL + "/login"
    payload = {"username": username_info, "password": password_info}
    response = requests.post(url, json=payload)

    if response.status_code == 200:
        # show success message on screen
        Label(login_screen, text="Login Success", fg="green", font=("calibri", 11)).pack()
    else:
        # show error message on screen
        Label(login_screen, text="Login Failed", fg="red", font=("calibri", 11)).pack()

def main():
    
    main_account_screen()

    main_screen.mainloop()


    
main()


