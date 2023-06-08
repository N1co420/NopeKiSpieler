import socketio
import json
import live_game
import printFormater
import time
## Creates a new instance of the SocketIO client
sio = socketio.Client()

topCard = None
hand= None
last_move = None
currentPlayer = None
last_TopCard = None
player_id = None


## Event handler for the SocketIO 'connect' event
@sio.event
def connect():
    print("connected")
    print("")

## Event handler for the SocketIO 'disconnect' event
@sio.event
def disconnect():
    print("disconected")
    print("")

## Event handler for a callback received from the server
# @param data The data received from the server
def callback(data):
    print(data)

@sio.on('list:tournaments')
def socket_tournament(list, namespace):
    tournaments = tournament_list(list)

@sio.on('tournament:playerInfo')
def socket_playerInfo(data, namespace):
    printFormater.printPlayerInfo(data)

@sio.on('tournament:info')
def tourn_info(data, namespace):
    printFormater.printTournInfo(data)


@sio.on('tournament:status')
def tourn_status(data, namespace):
    printFormater.printTournStatus(data)

@sio.on('game:state')
def game_status(state, namespace):
    #printFormater.printGameStatus(state)
    global topCard, hand, last_move, currentPlayer, last_TopCard, player_id

    topCard = state['topCard']
    last_TopCard = state['lastTopCard']
    last_move = state['last_move']
    hand = state['hand']
    currentPlayer = state['currentPlayer']
    player_id = state['player_id']

    if player_id == currentPlayer['id']:
        print("HANDKARTEN:  ")
        for card in state['hand']:
            print(card['type'], card['color'], card['value'])

@sio.on('make:move')
def make_move(data):
    global topCard, hand
    print(data['message'])
    move = None # ki_spieler.build_move()
    time.sleep(0.5)
    return move

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