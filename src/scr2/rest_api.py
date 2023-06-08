import requests
import json

user_id = None

# This function sends a POST request to register a new user with the server
def register(json_data):
    # Set the endpoint URL for registration
    url = "https://nope-server.azurewebsites.net/api/auth/register"
    # Send the POST request to the server and store the respons
    response = requests.post(url, json=json_data)
    # Check if the response status code indicates successful registration
    if response.status_code == 201:
        # Extract the registration success message from the response JSON
        json_response = response.json()
        return json_response["message"]
    else:
        # Return an error message if registration failed
        return f"Registration failed with status code {response.status_code}"

# This function sends a POST request to log in a user with the server
def login(data):
    # Set the endpoint URL for login
    url = "https://nope-server.azurewebsites.net/api/auth/login"
    # compare_data(json_data)
    # Send the POST request to the server and store the response
    response = requests.post(url, json=data)
    # Check if the response status code indicates successful login
    if response.status_code == 200:
        # Extract the access token from the response JSON
        json_response = response.json()

        global user_id
        access_token = json_response["accessToken"]
        user_id = json_response["user"]["id"]
        return access_token, user_id
    else:
        print(response)
        return None


def call_login():
    user = {"username": "nico2", "password": "654321"}
    result = login(user)

    if result:
        # Login successful, do something here
        print(result)
        print("eingloggt mit user")
    else:
        # Login failed, display error message to the user
        #error_label.config(text="Invalid username or password")
        print(result)

# This function demonstrates how to call the register_user function and handle the result
def call_register():
    # Attempt to register a new test account
    
    data = {"username": "nico2", "password": "654321", "firstname": "nico2", "lastname": "huebner"}

    result = register(data)
    # Print the result of the registration attempt
    print(result)