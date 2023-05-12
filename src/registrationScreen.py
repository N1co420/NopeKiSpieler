# This File is the implementation of a screen for user registration
from tkinter import*
import json
import register_login_User
import socketConnect
 
# set global variables

def main_account_screen():
    global main_screen
    main_screen = Tk() # create the GUI window
    main_screen.geometry("300x250") # set the configuration of the GUI window
    main_screen.title("Accoount Login") # set the title of the GUI window

    # create a form label
    Label(text="Choose Login Or Register", bg="blue", width="300", height="2").pack()
    Label(text="").pack()

    # create a login Button
    Button(text="login", height="2", width="30", command=login_gui).pack()
    Label(text="").pack()

    # create a reigster Button
    Button(text="Register", height="2", width="30", command=register_gui).pack()
    Label(text="").pack()

def test(register_data):
    print(register_data)

def register_gui():
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
    lastname_entry = Entry(register_screen, textvariable=lastname)
    lastname_entry.pack()

    Label(register_screen, text="").pack()

    # set register button
    Button(register_screen, text="Register now", width=10, height=1, bg="blue", command = lambda: register_user(transform2dict(username_entry, password_entry, firstname_entry, lastname_entry))).pack()

def login_gui():
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()
 
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

    Button(login_screen, text="Login", width=10, height=1, command= lambda: login_verification(transform2dict(username_login_entry, password__login_entry))).pack()
   
def login_verification(login_data):
    # Call the login_verification function from the register_login_User module
    result = register_login_User.login(login_data)
    test(login_data)
    
    if result:
        # Login successful, do something here
        print(result)
        socketConnect(result)
        pass
    else:
        # Login failed, display error message to the user
        #error_label.config(text="Invalid username or password")
        print(result)

def register_user(registration_data):
    # Call the register_user function from the register_login_User module
    result = register_login_User.register(registration_data)
    
    if result:
        # Registration successful, do something here
        print(registration_data)
        landingpage()
        pass
    else:
        # Registration failed, display error message to the user
        # error_label.config(text="Username already exists")
        print("error")

def transform2dict(username_entry, password_entry, firstname_entry=None, lastname_entry=None):
    """
    A function to transform user input data into a JSON string.

    Args:
        username_entry (Tkinter.Entry): An Entry widget for the username.
        password_entry (Tkinter.Entry): An Entry widget for the password.
        firstname_entry (Optional[Tkinter.Entry], optional): An Entry widget for the firstname. Defaults to None.
        lastname_lable (Optional[Tkinter.Label], optional): A Label widget for the lastname. Defaults to None.

    Returns:
        str: A Dictionary containing the username, password, firstname, and lastname (if provided).

    """
    # Get the values of the username and password entries
    username = username_entry.get()
    password = password_entry.get()

    # Create a dictionary with the username and password values
    data = {"username": username, "password": password}

    # Check if firstname and lastname widgets were provided
    if firstname_entry and lastname_entry:
        # Get the values of the firstname and lastname widgets
        firstname = firstname_entry.get()
        lastname = lastname_entry.get()
        # Add the firstname and lastname values to the data dictionary
        data["firstname"] = firstname
        data["lastname"] = lastname

    # Convert the data dictionary to a JSON string and return it
    
    return data


def landingpage():
    print("landing page")

def main():
    
    main_account_screen()

    main_screen.mainloop()


    
main()


