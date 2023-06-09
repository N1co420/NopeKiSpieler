import socketio
import requests

from sio_events import *

## Attempts to connect to the SocketIO server with the specified access token
# @param access_token The access token used to authenticate with the server
def connect_to_socketio_server(access_token):
    """
    Attempts to connect to the SocketIO server with the specified access token.

    Parameters:
        access_token (str): The access token used to authenticate with the server.

    Returns:
        None
    """
    try:
        # Connect to SocketIO server with access token
        sio.connect("https://nope-server.azurewebsites.net", namespaces="/", auth={"token": access_token})
    except requests.exceptions.RequestException as e:
        print(f'Failed to connect to SocketIO server: {e}')
    except socketio.exceptions.ConnectionError as e:
        print(f'Failed to connect to SocketIO server: {e}')
    except socketio.exceptions.BadNamespaceError as e:
        print(f'Failed to connect to SocketIO server: {e}')

#  Disconnect from the SocketIO server.
def disconnect_from_socketio_server():
    """
    Disconnects from the SocketIO server.

    Parameters:
        None

    Returns:
        None
    """
    try:
        sio.disconnect()
    except socketio.exceptions.ConnectionError as e:
        print(f'Failed to disconnect from SocketIO server: {e}')

## Creates a new tournament with the specified number of games
# @param num_games The number of games to be included in the tournament
def create_tournament(num_games):
    """
    Creates a new tournament with the specified number of games.

    Parameters:
        num_games (int): The number of games to be included in the tournament.

    Returns:
        None
    """
    try:
        response = sio.call("tournament:create",num_games)
        if response["success"]:
            print("Tournament created!")
            print(f"Tournament ID: {response['data']['tournamentId']}")
            print(f"Current size: {response['data']['currentSize']}")
            print(f"Best of: {response['data']['bestOf']}")
        else:
            print("Failed to create tournament.")
            print(f"Error message: {response['error']}")
    except Exception as e:
        print(f"Failed to create tournament: {e}")

## Joins a tournament with the specified ID
# @param tournament_id The ID of the tournament to join
def join_tournament(tournament_id): 
    """
    Joins a tournament with the specified ID.

    Parameters:
        tournament_id (str): The ID of the tournament to join.

    Returns:
        None
    """
    try:
        response= sio.call("tournament:join", tournament_id )
        callback(response)
    except socketio.exceptions.TimeoutError as e:
        print(f'Timeout error occurred: {e}')
    except socketio.exceptions.BadNamespaceError as e:
        print(f'Bad namespace error occurred: {e}')

## Starts a tournament with the specified ID
def start_tournament():
    """
    Starts a tournament with the specified ID.

    Parameters:
        None

    Returns:
        bool: True if the tournament started successfully, False otherwise.
    """
    try:
        response = sio.call("tournament:start")
        
        if response["success"]:
            print("Tournament started")
            return True 
        else:
            print(f"Tournament failed to start: {response['error']['message']}")

        print(f"Response: {response}")
    except Exception as e:
        print(f"Failed to start tournament: {e}")

## Leaves a tournament with the specified ID
def leave_tournament():
    """
    Leaves the current tournament.

    Parameters:
        None

    Returns:
        None
    """
    try:
        response = sio.call("tournament:leave")
        if response["success"]:
            print("You have left the tournament.")
        else:
            print("Failed to leave the tournament.")
            print(f"Error message: {response['error']}")
    except Exception as e:
        print(f"Failed to leave tournament: {e}")