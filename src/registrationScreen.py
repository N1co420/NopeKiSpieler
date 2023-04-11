# This File is the implementation of a screen for user registration
from tkinter import*
import json

def main_account_screen():
    global main_screen
    main_screen = Tk() # create the GUI window
    main_screen.geometry("300x250") # set the configuration of the GUI window
    main_screen.title("Accoount Login") # set the title of the GUI window

    # create a form label
    Label(text="Choose Login Or Register", bg="blue", width="300", height="2").pack()
    Label(text="").pack()

    # create a login Button
    Button(text="login", height="2", width="30").pack()
    Label(text="").pack()

    # create a reigster Button
    Button(text="Register", height="2", width="30", command=register).pack()

def register():
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
    Button(register_screen, text="Register", width=10, height=1, bg="blue").pack()


def main():
    
    main_account_screen()

    # register()

    main_screen.mainloop()


    
main()


