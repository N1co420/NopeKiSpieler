# Hauptmenü (`main_menu.py`) 

Die Datei `main_menu.py` enthält die Hauptfunktion des Spiels, die das Hauptmenü darstellt und die Benutzereingabe verarbeitet. 

### `mainMenu()`

Die Hauptfunktion des Spiels, die das Hauptmenü darstellt und die Benutzereingabe verarbeitet.

#### Ablauf

1. Verbindung zum Server herstellen: Die Funktion `rest_api.login()` wird verwendet, um den Benutzer am Server anzumelden.
2. Verbindung zum Socket.IO-Server herstellen: Die Funktion `tournament_handler.connect_to_socketio_server()` wird verwendet, um eine Verbindung zum Socket.IO-Server herzustellen.
3. Hauptschleife: Die Schleife wird solange ausgeführt, bis der Benutzer das Spiel beendet.
   - Menüoptionen anzeigen: Das Menü wird dem Benutzer angezeigt.
   - Benutzereingabe erhalten: Die Funktion `input()` wird verwendet, um die Benutzereingabe zu erhalten.
   - Verarbeitung der Benutzereingabe: Abhängig von der Benutzereingabe werden entsprechende Funktionen aus `tournament_handler.py` aufgerufen.
4. Spielende: Das Spiel endet.



Um zum Hauptmenü zurückzukehren, klicken Sie [hier](../README.md).