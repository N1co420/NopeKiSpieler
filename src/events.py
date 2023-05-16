import socketio
import json

## Creates a new instance of the SocketIO client
sio = socketio.Client()


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
def socket_tournament(list, namespace):
    tournaments = tournament_list(list)

@sio.on('tournament:playerInfo')
def socket_playerInfo(data, namespace):
    print("PLAYERINFO")
    print("Received tournament player info:")
    print(f"Tournament ID: {data['tournamentId']}")
    print(f"Current size: {data['currentSize']}")
    print(f"Best of: {data['bestOf']}")
    print("Players:")
    for player in data['players']:
        print(f" - ID: {player['id']}, username: {player['username']}")

@sio.on('tournament:info')
def tourn_info(data, namespace):
    print("TOURN INFO")
    print("Message: ", data)

@sio.on('tournament:status')
def tourn_status(data, namespace):
    print("TOURN STATUS")
    print(json.dumps(data, indent=4))

@sio.on('game:state')
def game_status(state, namespace):
    print("GAME STATUS")
    print(json.dumps(state, indent=4))

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