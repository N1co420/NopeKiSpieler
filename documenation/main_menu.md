# Hauptmenü (`main_menu.py`) und Zusammenarbeit mit anderen Dateien

Die Datei `main_menu.py` enthält die Hauptfunktion des Spiels, die das Hauptmenü darstellt und die Benutzereingabe verarbeitet. Sie arbeitet eng mit anderen Dateien zusammen, um verschiedene Funktionen auszuführen. Hier ist eine Übersicht über die Zusammenarbeit mit anderen Dateien:

## Abhängigkeiten

Die Datei `main_menu.py` hängt von den folgenden Dateien ab:

- [`rest_api.py`](rest_api.md): Wird für die Verbindung zum Server und die Benutzerauthentifizierung verwendet.
- [`tournament_handler.py`](tournament_handler.md): Enthält Funktionen zur Verwaltung von Turnieren und zur Kommunikation mit dem Server.
- [`game_rules.py`](game_rules.md): Enthält Spielregeln und Funktionen für das Spiel.
- [`payload_builder.py`](payload_builder.md): Wird verwendet, um Payloads für die Kommunikation mit dem Server aufzubauen.
- [`sio_events.py`](sio_events.md): Enthält Funktionen zur Verarbeitung von Socket.IO-Ereignissen.
- [`ki_spieler.py`](ki_spieler.md): Enthält Funktionen für KI-Spieler-Strategien.

## Verwendete Funktionen

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



