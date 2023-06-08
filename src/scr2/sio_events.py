import socketio
import json
import time
import console_formater
## Get UserID
from rest_api import user_id
## Creates a new instance of the SocketIO client
sio = socketio.Client()

topCard = None
last_TopCard = None
last_move = None
hand = None
currentPlayer = None

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
    tournaments = console_formater.tournament_list(list)
    print(list)

@sio.on('tournament:playerInfo')
def socket_playerInfo(data, namespace):
    console_formater.printPlayerInfo(data)
    print(data)

@sio.on('tournament:info')
def tourn_info(data, namespace):
    console_formater.printTournInfo(data)
    print(data)

@sio.on('tournament:status')
def tourn_status(data, namespace):
    #printFormater.printTournStatus(data)
    print(data)

@sio.on('game:state')
def game_state(data, namespace):
    #printFormater.printGameStatus(state)
    global topCard, hand, last_move, currentPlayer, last_TopCard

    topCard = data['topCard']
    last_TopCard = data['lastTopCard']
    last_move = data['lastMove']
    hand = data['hand']
    currentPlayer = data['currentPlayer']
    
    if user_id == currentPlayer['id']:
        print("HANDKARTEN:  ")
        for card in data['hand']:
            print(card['type'], card['color'], card['value'])

@sio.on('game:status')
def game_status(data, namespace):
    print(data)

@sio.on('make:move')
def make_move(data, namespace):
    global topCard, hand
    print(data['message'])
    move = None # ki_spieler.build_move()
    time.sleep(0.5)
    return move