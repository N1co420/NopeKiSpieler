import socketio
import payload
import game_logic
from events import sio, game_status


def handle_game_status():
    # Extract necessary information from the game status data
    player_id = game_status['playerID']
    current_player_id = game_status['currentPlayerID']
    hand = game_status['hand']
    top_card = game_status['topCard']
    last_top_card = game_status['lastTopCard']

    return current_player_id, hand, top_card, last_top_card

def play_game(jwt_token, player_id):

    while (True):

        current_player_id, hand, top_card, last_top_card = handle_game_status()

        if game_logic.myTurn(player_id, current_player_id):
            
            print("Its My Turn!")
            move_payload = payload.buildPayload("take")
            
            payload.send_payload(move_payload)
            # build payload
            
