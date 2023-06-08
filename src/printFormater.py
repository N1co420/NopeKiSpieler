import json 

def printPlayerInfo(data):
    print("PLAYERINFO")
    print("Received tournament player info:")
    print(f"Tournament ID: {data['tournamentId']}")
    print(f"Current size: {data['currentSize']}")
    print(f"Best of: {data['bestOf']}")
    print("Players:")
    for player in data['players']:
        print(f" - ID: {player['id']}, username: {player['username']}")
    print("")

def printTournInfo(data):
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

def printTournStatus(data):
    print("TOURN STATUS")
    print(json.dumps(data, indent=4))

def printGameStatus(state):
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