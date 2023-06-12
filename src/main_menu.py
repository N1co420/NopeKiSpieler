
import rest_api
import tournament_handler

def mainMenu():
    """
    The main menu function for the game.

    Connects to the server, displays a menu, and handles user input.

    :return: None
    """
    # Connect to the server
    user = {"username": "nico", "password": "654321"}
    result, id = rest_api.login(user)

    tournament_handler.connect_to_socketio_server(result)

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
            tournament_handler.create_tournament(num_games)
        elif choice == "w":
            tournament_id = input("Enter the tournament ID: ")
            tournament_handler.join_tournament(tournament_id)
        elif choice == "e":
            result = tournament_handler.start_tournament()
            if result == True:
                print("STARTED:")
        elif choice == "r":
            tournament_handler.leave_tournament()
        elif choice == "t":
            tournament_handler.disconnect_from_socketio_server()
            break
        else:
            print("Invalid choice. Please try again.")

mainMenu()