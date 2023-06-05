import socketio
import payload
import game_logic
from events import *


def handle_game_status(data):
    # Extract necessary information from the game status data
    player_id = data['playerID']
    current_player_id = data['currentPlayerID']
    hand = data['hand']
    top_card = data['topCard']
    last_top_card = data['lastTopCard']

    return current_player_id, hand, top_card, last_top_card

def play_game(jwt_token, player_id):

    while (True):
        sio.on("game:state", game_status)

        current_player_id, hand, top_card, last_top_card = handle_game_status(game_status)

        if game_logic.myTurn(player_id, current_player_id):
            
            cards = game_logic.makeMove(hand, top_card, last_top_card)
            
            # build payload
            
