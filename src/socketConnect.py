import socketio
import requests
import register_login_User

## Creates a new instance of the SocketIO client
sio = socketio.Client()

## Attempts to connect to the SocketIO server with the specified access token
# @param access_token The access token used to authenticate with the server
def connect_to_socketio_server(access_token):
    try:
        # Connect to SocketIO server with access token
        sio.connect("https://nope-server.azurewebsites.net", namespaces="/", auth={"token": access_token})
    except requests.exceptions.RequestException as e:
        print(f'Failed to connect to SocketIO server: {e}')
    except socketio.exceptions.ConnectionError as e:
        print(f'Failed to connect to SocketIO server: {e}')
    except socketio.exceptions.BadNamespaceError as e:
        print(f'Failed to connect to SocketIO server: {e}')

#  Disconnect from the SocketIO server.
def disconnect_from_socketio_server():
    try:
        sio.disconnect()
    except socketio.exceptions.ConnectionError as e:
        print(f'Failed to disconnect from SocketIO server: {e}')


## Creates a new tournament with the specified number of games
# @param num_games The number of games to be included in the tournament
def create_tournament(num_games):
    try:
        response = sio.call("tournament:create",num_games)
        callback(response)
    except Exception as e:
        print(f"Failed to create tournament: {e}")

## Joins a tournament with the specified ID
# @param tournament_id The ID of the tournament to join
def join_tournament(tournament_id): 
    try:
        response= sio.call("tournament:join", tournament_id )
        callback(response)
    except socketio.exceptions.TimeoutError as e:
        print(f'Timeout error occurred: {e}')
    except socketio.exceptions.BadNamespaceError as e:
        print(f'Bad namespace error occurred: {e}')

## Starts a tournament with the specified ID
# @param tournament_id The ID of the tournament to start
def start_tournamet(tournament_id):
    try:
        response = sio.call("tournament:start", tournament_id)
        
    except Exception as e:
        print(f"Failed to start tournament: {e}")

## Leaves a tournament with the specified ID
# @param tournament_id The ID of the tournament to leave
def leave_tournament(tournament_id):
    try:
        response = sio.call("tournament:leave", tournament_id)
        
    except Exception as e:
        print(f"Failed to leave tournament: {e}")

## Formats and prints a list of tournaments received from the server
# @param data The data received from the server, containing a list of tournaments
# @return The list of tournaments as a dictionary
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
    return tournaments

## Event handler for the SocketIO 'connect' event
@sio.event
def connect():
    print("connected")

## Event handler for the SocketIO 'disconnect' event
@sio.event
def disconnect():
    print("disconected")

## Event handler for a callback received from the server
# @param data The data received from the server
def callback(data):
    print(data)

@sio.on('list:tournaments')
def socket_on(list, namespace):
    tournaments = tournament_list(list)

def main():
    user = {"username": "nico", "password": "654321"}
    result = register_login_User.login(user)

    connect_to_socketio_server(result)


    disconnect_from_socketio_server()
    

main()

