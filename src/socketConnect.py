import socketio
import requests
import register_login_User

sio = socketio.Client() 

def connect_to_socketio_server(access_token):
    try:
        # Connect to SocketIO server with access token
        
        # headers = {'Authorization': 'Bearer ' + access_token}
        sio.connect("https://nope-server.azurewebsites.net", namespaces="/", auth={'token': access_token})
        # sio.connect('https://nope-server.azurewebsites.net', headers={'Authorization': 'Bearer ' + access_token})

        
        # Wait for events to be emitted and received
        # sio.wait()
    except requests.exceptions.RequestException as e:
        print(f'Failed to connect to SocketIO server: {e}')
    except socketio.exceptions.ConnectionError as e:
        print(f'Failed to connect to SocketIO server: {e}')
    except socketio.exceptions.BadNamespaceError as e:
        print(f'Failed to connect to SocketIO server: {e}')

@sio.event
def connect():
    print("connected")

@sio.event
def disconnect():
    print("disconected")

@sio.event
def callback(data):
    print(data)

@sio.on('list:tournaments')
def socket_on(data):
    print("list")
    #print(data)
# Define the callback function
def on_response(data):
    # print and save data here
    print("Response:", data)
    # save data to a file or database
    # ...

# Function to create a tournament
def create_tournament(num_games):
    response = sio.call("tournament:create",num_games)
    print(response)

# Function to join a tournament
def join_tournament(): #tournament_id
    response= sio.call("tournament:join", 'clh4zo1ke000gnx07b5hrzk8l' )
    print(response)

def leave_tournament():
    response = sio.call("tournament:leave")
    print(response)

def main():
    user = {"username": "nico", "password": "654321"}
    result = register_login_User.login(user)

    connect_to_socketio_server(result)
    
    join_tournament()
    leave_tournament()
    #create_tournament(3)



main()

