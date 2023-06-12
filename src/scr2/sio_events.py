import socketio
import json
import time
import console_formater
## Get UserID
from rest_api import user_id
from kiSpieler import kiPlayerAll
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

@sio.on('tournament:playerInfo')
def socket_playerInfo(data, namespace):
    console_formater.printPlayerInfo(data)
    print(data)

@sio.on('tournament:info')
def tourn_info(data, namespace):
    console_formater.printTournInfo(data)

@sio.on('tournament:status')
def tourn_status(data, namespace):
    #printFormater.printTournStatus(data)
    print("TOURN STATUS")
    print(data)
    print(" ")

@sio.on('game:state')
def game_state(data, namespace):
    global topCard, hand, last_move, currentPlayer, last_TopCard
    
    topCard = data['topCard']
    last_TopCard = data['lastTopCard']
    last_move = data['lastMove']
    hand = data['hand']
    currentPlayer = data['currentPlayer']

    console_formater.printGameState(data)

@sio.on('game:status')
def game_status(data, namespace):
    print("GAME STATUS")
    print(data)
    print(" ")

@sio.on('game:makeMove')
def make_move(data):
    print("MAKEMOVE")
    global topCard, hand, last_TopCard

    print(data['message'])
    move = kiPlayerAll(hand, topCard, last_TopCard)
    print(move)
    print(" ")
    time.sleep(0.5)
    return move