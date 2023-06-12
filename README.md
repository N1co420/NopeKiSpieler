python-ki player 
================

Python implementation of an ki-player designed to play the card game node

The following features should be implemented:
- Login and Registration of a User via the REST API
- Connecting to a Websocket via the socket-IO Framework


https://spiced-bayberry-f17.notion.site/Projekttagebuch-d291802969b9402bb81d89667fd50842

https://spiced-bayberry-f17.notion.site/KI-Spieler-7044f2518dd54e749bcaaaaa02f1242d

# python-ki player

Dieses Projekt enthält den Quellcode und die Dokumentation für das Spielprojekt.

## Projektbeschreibung

Das Spielprojekt ist eine interaktive Anwendung, die ein Kartenspiel simuliert. Spieler können an Turnieren teilnehmen, gegen KI-Spieler antreten und ihre Strategien entwickeln, um das Spiel zu gewinnen. Das Projekt besteht aus mehreren Modulen, die zusammenarbeiten, um das Spiel zu ermöglichen.

## Projektstruktur

Das Projekt besteht aus folgenden Dateien:

- [`main_menu.py`](src/main_menu.py): Das Hauptmenü des Spiels, das den Benutzern verschiedene Optionen bietet.
- [`game_rules.py`](src/game_rules.py): Die Spielregeln und Logik des Kartenspiels.
- [`ki_spieler.py`](src/ki_spieler.py): Implementierungen von KI-Spielern mit unterschiedlichen Strategien.
- [`payload_builder.py`](src/payload_builder.py): Hilfsfunktionen zum Erstellen von Datenpaketen für Spielzüge.
- [`sio_events.py`](src/sio_events.py): Ereignisbehandlung für die Socket.IO-Kommunikation mit dem Server.
- [`rest_api.py`](src/rest_api.py): Implementierung der REST-API für die Kommunikation mit dem Server.
- [`tournament_handler.py`](src/tournament_handler.py): Verwaltung von Turnieren und Spielrunden.

## Dokumentation

Die ausführliche Dokumentation des Projekts finden Sie im `documentation/`-Verzeichnis. Jede Datei in diesem Verzeichnis enthält eine detaillierte Beschreibung eines bestimmten Aspekts des Projekts, einschließlich Funktionen, Verwendungen und Beispielen. Hier sind die vorhandenen Dokumentationsdateien:

- [`main_menu.md`](documentation/main_menu.md): Dokumentation der Hauptmenu Funktionen.
- [`game_rules.md`](documentation/game_rules.md): Dokumentation der Spielregeln und der Logikfunktionen.
- [`ki_spieler.md`](documentation/ki_spieler.md): Dokumentation der verschiedenen KI-Spieler und ihrer Strategien.
- [`payload_builder.md`](documentation/payload_builder.md): Dokumentation der Funktionen zum Erstellen von Datenpaketen.
- [`sio_events.md`](documentation/sio_events.md): Dokumentation der Ereignisbehandlung für Socket.IO-Kommunikation.
- [`rest_api.md`](documentation/rest_api.md): Dokumentation der REST-API-Funktionen für die Serverkommunikation.
- [`tournament_handler.md`](documentation/tournament_handler.md): Dokumentation des Turniermanagements und der Spielrunden.



