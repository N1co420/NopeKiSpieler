# tournament_handler.py

Die Datei `tournament_handler.py` enthält Funktionen zum Interagieren mit Turnieren unter Verwendung von SocketIO.

### Import
- `socketio`: Das SocketIO-Modul zum Verbinden mit dem Server und Durchführen von Aufrufen.
- `requests`: Das Requests-Modul zum Verarbeiten von HTTP-Anfragen.
- `sio_events`: Der Import von Ereignis-Handler-Funktionen aus der Datei `sio_events.py`.

### Funktionen
1. `connect_to_socketio_server(access_token)`
   - Versucht, eine Verbindung zum SocketIO-Server mit dem angegebenen Zugriffstoken herzustellen.
   - Verbindet sich mit dem Server unter Verwendung des angegebenen Zugriffstokens und der Authentifizierung.
   - Gibt eine Fehlermeldung aus, wenn die Verbindung fehlschlägt.

2. `disconnect_from_socketio_server()`
   - Trennt die Verbindung zum SocketIO-Server.
   - Gibt eine Fehlermeldung aus, wenn die Trennung fehlschlägt.

3. `create_tournament(num_games)`
   - Erstellt ein neues Turnier mit der angegebenen Anzahl von Spielen.
   - Ruft den Server auf, um ein neues Turnier zu erstellen.
   - Gibt die Details des Turniers aus, wenn die Erstellung erfolgreich ist.
   - Gibt eine Fehlermeldung aus, wenn die Erstellung fehlschlägt.

4. `join_tournament(tournament_id)`
   - Tritt einem Turnier mit der angegebenen ID bei.
   - Ruft den Server auf, um dem Turnier beizutreten.
   - Gibt die Antwort des Servers aus.

5. `start_tournament()`
   - Startet ein Turnier.
   - Ruft den Server auf, um das Turnier zu starten.
   - Gibt eine Erfolgsmeldung aus, wenn das Turnier erfolgreich startet.
   - Gibt eine Fehlermeldung aus, wenn das Turnier nicht gestartet werden kann.

6. `leave_tournament()`
   - Verlässt das aktuelle Turnier.
   - Ruft den Server auf, um das Turnier zu verlassen.
   - Gibt eine Erfolgsmeldung aus, wenn das Verlassen des Turniers erfolgreich ist.
   - Gibt eine Fehlermeldung aus, wenn das Verlassen des Turniers fehlschlägt.


Um zum Hauptmenü zurückzukehren, klicken Sie [hier](main_menu.md).
