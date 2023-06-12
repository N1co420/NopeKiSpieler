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

@sio.event
def connect():
    """
    Event handler for the 'connect' event received from the SocketIO server.

    Parameters:
        None

    Returns:
        None
    """
    print("connected")
    print("")

@sio.event
def disconnect():
    """
    Event handler for the 'disconnect' event received from the SocketIO server.

    Parameters:
        None

    Returns:
        None
    """
    print("disconected")
    print("")

## Event handler for a callback received from the server
# @param data The data received from the server
def callback(data):
    """
    Event handler for a callback received from the server.

    Parameters:
        data (dict): The data received from the server.

    Returns:
        None
    """
    print(data)

@sio.on('list:tournaments')
def socket_tournament(list, namespace):
    """
    Event handler for the 'list:tournaments' event received from the SocketIO server.

    Parameters:
        list (list): The list of tournaments received from the server.
        namespace (str): The namespace of the event.

    Returns:
        None
    """
    tournaments = console_formater.tournament_list(list)

@sio.on('tournament:playerInfo')
def socket_playerInfo(data, namespace):
    """
    Event handler for the 'tournament:playerInfo' event received from the SocketIO server.

    Parameters:
        data (dict): The player information data received from the server.
        namespace (str): The namespace of the event.

    Returns:
        None
    """
    console_formater.printPlayerInfo(data)
    

@sio.on('tournament:info')
def tourn_info(data, namespace):
    """
    Event handler for the 'tournament:info' event received from the SocketIO server.

    Parameters:
        data (dict): The tournament information data received from the server.
        namespace (str): The namespace of the event.

    Returns:
        None
    """
    console_formater.printTournInfo(data)

@sio.on('tournament:status')
def tourn_status(data, namespace):
    """
    Event handler for the 'tournament:status' event received from the SocketIO server.

    Parameters:
        data (dict): The tournament status data received from the server.
        namespace (str): The namespace of the event.

    Returns:
        None
    """
    #printFormater.printTournStatus(data)
    print("TOURN STATUS")
    print(data)
    print(" ")

@sio.on('game:state')
def game_state(data, namespace):
    """
    Event handler for the 'game:state' event received from the SocketIO server.

    Parameters:
        data (dict): The game state data received from the server.
        namespace (str): The namespace of the event.

    Returns:
        None
    """
    global topCard, hand, last_move, currentPlayer, last_TopCard
    
    topCard = data['topCard']
    last_TopCard = data['lastTopCard']
    last_move = data['lastMove']
    hand = data['hand']
    currentPlayer = data['currentPlayer']

    console_formater.printGameState(data)

@sio.on('game:status')
def game_status(data, namespace):
    """
    Event handler for the 'game:status' event received from the SocketIO server.

    Parameters:
        data (dict): The game status data received from the server.
        namespace (str): The namespace of the event.

    Returns:
        None
    """
    print("GAME STATUS")
    print(data)
    print(" ")

@sio.on('game:makeMove')
def make_move(data):
    """
    Event handler for the 'game:makeMove' event received from the SocketIO server.

    Parameters:
        data (dict): The data related to the 'makeMove' event received from the server.

    Returns:
        move: The move to be made.
    """
    print("MAKEMOVE")
    global topCard, hand, last_TopCard

    print(data['message'])
    move = kiPlayerAll(hand, topCard, last_TopCard)
    print(move)
    print(" ")
    time.sleep(0.5)
    return move