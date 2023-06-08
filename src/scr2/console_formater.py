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