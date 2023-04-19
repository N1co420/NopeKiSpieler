import requests

# This function sends a POST request to register a new user with the server
def register(json_data):
    # Set the endpoint URL for registration
    url = "https://nope-server.azurewebsites.net/api/auth/register"
    # Send the POST request to the server and store the response
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
def login(json_data):
    # Set the endpoint URL for login
    url = "https://nope-server.azurewebsites.net/api/auth/login"
    
    # Send the POST request to the server and store the response
    response = requests.post(url, json=json_data)
    # Check if the response status code indicates successful login
    if response.status_code == 200:
        # Extract the access token from the response JSON
        json_response = response.json()
        access_token = json_response["accessToken"]
        return access_token
    else:
        # Return None if login failed
        return None

# This function demonstrates how to call the login function and handle the result
def call_login():
    # Attempt to log in with the test account
    access_token = login("demicas", "552000")
    # Check if login was successful
    if access_token:
        print("Login successful!")
    else:
        print("Login failed.")

# This function demonstrates how to call the register_user function and handle the result
def call_register():
    # Attempt to register a new test account
    result = register("demicas", "552000", "nico", "huebner")
    # Print the result of the registration attempt
    print(result)


