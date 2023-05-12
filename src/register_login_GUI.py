import tkinter as tk
from register_login_User import register_user, login


def register_button_click():
    result = register_user(username_entry.get(), password_entry.get(), firstname_entry.get(), lastname_entry.get())
    result_label.config(text=result)


def login_button_click():
    access_token = login(username_entry.get(), password_entry.get())
    if access_token:
        result_label.config(text="Login successful!")
    else:
        result_label.config(text="Login failed.")


# Create the main window
window = tk.Tk()
window.title("REST API Registration and Login")

# Create the input fields
username_label = tk.Label(window, text="Username:")
username_label.pack()
username_entry = tk.Entry(window)
username_entry.pack()

password_label = tk.Label(window, text="Password:")
password_label.pack()
password_entry = tk.Entry(window, show="*")
password_entry.pack()

firstname_label = tk.Label(window, text="First Name:")
firstname_label.pack()
firstname_entry = tk.Entry(window)
firstname_entry.pack()

lastname_label = tk.Label(window, text="Last Name:")
lastname_label.pack()
lastname_entry = tk.Entry(window)
lastname_entry.pack()

# Create the buttons
register_button = tk.Button(window, text="Register", command=register_button_click)
register_button.pack()

login_button = tk.Button(window, text="Login", command=login_button_click)
login_button.pack()

# Create the result label
result_label = tk.Label(window, text="")
result_label.pack()

# Run the main loop
window.mainloop()
