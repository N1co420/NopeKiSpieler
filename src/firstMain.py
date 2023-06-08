import socketio
import requests
import live_game
import register_login_User
import socketConnect
from events import *
import printFormater

def main():
    # Connect to the server
    user = {"username": "nico", "password": "654321"}
    result, id = register_login_User.login(user)

    socketConnect.connect_to_socketio_server(result)

    while True:
        # Display menu options
        print("Menu:")
        print("q. Create Tournament")
        print("w. Join Tournament")
        print("e. Start Tournament")
        print("r. Leave Tournament")
        print("t. Disconnect")

        # Get user input
        choice = input("Enter your choice: ")

        if choice == "q":
            num_games = int(input("Enter the number of games: "))
            socketConnect.create_tournament(num_games)
        elif choice == "w":
            tournament_id = input("Enter the tournament ID: ")
            socketConnect.join_tournament(tournament_id)
        elif choice == "e":
            result = socketConnect.start_tournament()
            if result == True:
                print("STARTED:")
        elif choice == "r":
            socketConnect.leave_tournament()
        elif choice == "t":
            socketConnect.disconnect_from_socketio_server()
            break
        else:
            print("Invalid choice. Please try again.")

        


main()