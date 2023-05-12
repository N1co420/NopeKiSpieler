import socketio
import requests

class SocketIOClient:
    def __init__(self, access_token):
        self.access_token = access_token
        self.sio = socketio.Client()
        
        self.sio.on('connect', self._on_connect)
        self.sio.on('disconnect', self._on_disconnect)
        self.sio.on('callback', self._on_callback)
        self.sio.on('list:tournaments', self._on_list_tournaments)

    def _on_connect(self):
        print("connected")

    def _on_disconnect(self):
        print("disconnected")

    def _on_callback(self, data):
        print(data)

    def _on_list_tournaments(self, data):
        tournaments = self._tournament_list(data)
        # do something with the tournaments

    def _tournament_list(self, data):
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

    def connect(self):
        try:
            self.sio.connect(
                "https://nope-server.azurewebsites.net",
                namespaces="/",
                auth={"token": self.access_token}
            )
        except (requests.exceptions.RequestException, socketio.exceptions.ConnectionError, socketio.exceptions.BadNamespaceError) as e:
            print(f'Failed to connect to SocketIO server: {e}')

    def disconnect(self):
        self.sio.disconnect()

    def create_tournament(self, num_games):
        try:
            response = self.sio.call("tournament:create", num_games)
            self._on_callback(response)
        except Exception as e:
            print(f"Failed to create tournament: {e}")

    def join_tournament(self, tournament_id): 
        try:
            response = self.sio.call("tournament:join", tournament_id)
            self._on_callback(response)
        except socketio.exceptions.TimeoutError as e:
            print(f'Timeout error occurred: {e}')
        except socketio.exceptions.BadNamespaceError as e:
            print(f'Bad namespace error occurred: {e}')

    def start_tournament(self, tournament_id):
        try:
            response = self.sio.call("tournament:start", tournament_id)
        except Exception as e:
            print(f"Failed to start tournament: {e}")

    def leave_tournament(self, tournament_id):
        try:
            response = self.sio
        except Exception as e:
            print(f"Failed to leave tournament: {e}")
