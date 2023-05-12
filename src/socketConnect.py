import socketio
import requests
import register_login_User

sio = socketio.Client() 

def connect_to_socketio_server(access_token):
    try:
        # Connect to SocketIO server with access token
        
        # headers = {'Authorization': 'Bearer ' + access_token}
        sio.connect("https://nope-server.azurewebsites.net", namespaces="/", auth={"token": access_token})
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
def socket_on(list, namespace):
    tournament_list(list)
# Define the callback function


# Function to create a tournament
def create_tournament(num_games):
    response = sio.call("tournament:create",num_games)
    print(response)

# Function to join a tournament
def join_tournament(tournament_id): 
    response= sio.call("tournament:join", tournament_id )
    print(response)

def start_tournamet():
    response= sio.call("tournament:start")
    print(response)

def leave_tournament():
    response = sio.call("tournament:leave")
    print(response)


def tournament_list(data):

    # Create an empty dictionary to store the tournament data
    tournaments = {}

    # Loop through each tournament dictionary in the list and add it to the tournaments dictionary using its ID as the key
    for tournament in data:
        tournaments[tournament['id']] = tournament

    # Iterate through the tournaments dictionary and print each tournament's details
    for i, (tournament_id, tournament_details) in enumerate(tournaments.items()):
        players = ", ".join([player['username'] for player in tournament_details['players']])
        print(f"{i+1}. Tournament ID: {tournament_id}")
        print(f"Status: {tournament_details['status']}")
        print(f"Players: {players}")
        print("")

    


def main():
    user = {"username": "nico", "password": "654321"}
    result = register_login_User.login(user)

    connect_to_socketio_server(result)
    
    #create_tournament(3)
    #start_tournamet()
    join_tournament("clhkk20pa0002p907i4uxdca0")
    leave_tournament()
    #create_tournament(3)



main()

