import socketio
import payload
import game_logic


def handle_game_status(data):
    # Extract necessary information from the game status data
    player_id = data['playerID']
    current_player_id = data['currentPlayerID']
    hand = data['hand']
    top_card = data['topCard']
    last_top_card = data['lastTopCard']

def play_game(jwt_token, player_id):
    # Authenticate with the server and retrieve the initial game status using the provided token and player ID
    initial_game_status = get_initial_game_status(jwt_token, player_id)

    # Handle the initial game status
    handle_game_status(initial_game_status)

    # Game loop
    while not game_over:
        # Check if it's the client's turn
        if game_logic.myTurn(player_id, current_player_id):
            # Determine the move to be made using game logic
            move = game_logic.makeMove(hand, top_card, last_top_card)

            # Build the move payload
            move_payload = payload.buildPayload(move.type, move.cards, move.select_color)

            # Send the move payload to the server
            payload.send_payload(move_payload)

        # Wait for the next game status update from the server
        new_game_status = wait_for_game_status_update()

        # Handle the new game status
        handle_game_status(new_game_status)