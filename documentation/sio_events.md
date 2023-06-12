# sio_events.py

Die Datei `sio_events.py` enthält Event-Handler-Funktionen für Ereignisse, die von einem SocketIO-Server empfangen werden.

### Importe
- `socketio`: Das SocketIO-Modul zur Verbindung mit dem Server und zum Empfangen von Ereignissen.
- `json`: Das JSON-Modul zum Verarbeiten von JSON-Daten.
- `time`: Das Zeitmodul zum Hinzufügen von Verzögerungen zwischen Aktionen.
- `console_formater`: Ein Modul für die Konsolenausgabe von formatierten Daten.
- `rest_api`: Der Import der `user_id`-Variable aus der `rest_api.py`-Datei.

### Variablen
- `topCard`: Eine Variable, die den aktuellen obersten Spielkartenwert speichert.
- `last_TopCard`: Eine Variable, die den vorherigen obersten Spielkartenwert speichert.
- `last_move`: Eine Variable, die den letzten Spielzug speichert.
- `hand`: Eine Variable, die die aktuelle Hand des Spielers speichert.
- `currentPlayer`: Eine Variable, die den aktuellen Spieler speichert.

### Event-Handler-Funktionen
1. `connect()`
   - Event-Handler für das 'connect'-Ereignis, das vom SocketIO-Server empfangen wird.
   - Wird aufgerufen, wenn eine Verbindung zum Server hergestellt wurde.

2. `disconnect()`
   - Event-Handler für das 'disconnect'-Ereignis, das vom SocketIO-Server empfangen wird.
   - Wird aufgerufen, wenn die Verbindung zum Server getrennt wurde.

3. `callback(data)`
   - Event-Handler für einen Rückruf (callback), der vom Server empfangen wird.
   - Wird aufgerufen, wenn ein allgemeiner Rückruf vom Server empfangen wird.
   - Gibt die empfangenen Daten aus.

4. `socket_tournament(list, namespace)`
   - Event-Handler für das 'list:tournaments'-Ereignis, das vom SocketIO-Server empfangen wird.
   - Wird aufgerufen, wenn eine Liste von Turnieren empfangen wird.
   - Formatiert und gibt die Turnierliste aus.

5. `socket_playerInfo(data, namespace)`
   - Event-Handler für das 'tournament:playerInfo'-Ereignis, das vom SocketIO-Server empfangen wird.
   - Wird aufgerufen, wenn Informationen zu einem Spieler in einem Turnier empfangen werden.
   - Formatiert und gibt die Spielerinformationen aus.

6. `tourn_info(data, namespace)`
   - Event-Handler für das 'tournament:info'-Ereignis, das vom SocketIO-Server empfangen wird.
   - Wird aufgerufen, wenn Informationen zu einem Turnier empfangen werden.
   - Formatiert und gibt die Turnierinformationen aus.

7. `tourn_status(data, namespace)`
   - Event-Handler für das 'tournament:status'-Ereignis, das vom SocketIO-Server empfangen wird.
   - Wird aufgerufen, wenn der Status eines Turniers empfangen wird.
   - Gibt den Turnierstatus aus.

8. `game_state(data, namespace)`
   - Event-Handler für das 'game:state'-Ereignis, das vom SocketIO-Server empfangen wird.
   - Wird aufgerufen, wenn der Spielzustand empfangen wird.
   - Aktualisiert die globalen Variablen `topCard`, `last_TopCard`, `last_move`, `hand` und `currentPlayer`.
   - Formatiert und gibt den Spielzustand aus.

9. `game_status(data, namespace)`
   - Event-Handler für das 'game:status'-Ereignis, das vom SocketIO-Server empfangen wird.
   - Wird aufgerufen, wenn der Status des Spiels empfangen wird.
   - Gibt den Spielstatus aus.

10. `make_move(data)`
    - Event-Handler für das 'game:makeMove'-Ereignis, das vom SocketIO-Server empfangen wird.
    - Wird aufgerufen, wenn ein Zug gemacht werden soll.
    - Ruft die `kiPlayerAll()`-Funktion auf, um einen Zug zu generieren.
    - Gibt den generierten Zug aus und gibt ihn zurück.



Um zum Hauptmenü zurückzukehren, klicken Sie [hier](../README.md).
