import socketio
import json

## Creates a new instance of the SocketIO client
sio = socketio.Client()


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
    print("PLAYERINFO")
    print("Received tournament player info:")
    print(f"Tournament ID: {data['tournamentId']}")
    print(f"Current size: {data['currentSize']}")
    print(f"Best of: {data['bestOf']}")
    print("Players:")
    for player in data['players']:
        print(f" - ID: {player['id']}, username: {player['username']}")
    print("")

@sio.on('tournament:info')
def tourn_info(data, namespace):
    print("TOURN INFO")
    print("Message: ", data['message'])
    print("Tournament ID: ", data['tournamentId'])
    print("Current Size: ", data['currentSize'])
    print("Status: ", data['status'])
    print("Players:")
    for player in data['players']:
        print(" - ID:", player['id'])
        print("   Username:", player['username'])
        print("   Score:", player['score'])
    print("Winner: ", data['winner'])
    print("Host:")
    print(" - ID:", data['host']['id'])
    print("   Username:", data['host']['username'])
    print("")


@sio.on('tournament:status')
def tourn_status(data, namespace):
    print("TOURN STATUS")
    print(json.dumps(data, indent=4))

@sio.on('game:state')
def game_status(state, namespace):
    print("GAME STATUS")
    print("Match ID:", state['matchId'])
    print("Game ID:", state['gameId'])
    print("Top Card:")
    print(" - Type:", state['topCard']['type'])
    print(" - Color:", state['topCard']['color'])
    print(" - Value:", state['topCard']['value'])
    print("Last Top Card:", state['lastTopCard'])
    print("Draw Pile Size:", state['drawPileSize'])
    print("Players:")
    for player in state['players']:
        print(" - ID:", player['id'])
        print("   Username:", player['username'])
        print("   Hand Size:", player['handSize'])
    print("Hand:")
    for card in state['hand']:
        print(" - Type:", card['type'])
        print("   Color:", card['color'])
        print("   Value:", card['value'])
    print("Hand Size:", state['handSize'])
    print("Current Player:")
    print(" - ID:", state['currentPlayer']['id'])
    print("   Username:", state['currentPlayer']['username'])
    print("Current Player Index:", state['currentPlayerIdx'])
    print("Previous Player:", state['prevPlayer'])
    print("Previous Player Index:", state['prevPlayerIdx'])
    print("Previous Turn Cards:", state['prevTurnCards'])
    print("Last Move:", state['lastMove'])
    print("")

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