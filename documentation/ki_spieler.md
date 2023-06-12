# kiSpieler.py

Die Datei `kiSpieler.py` enthält Funktionen, die die Spielstrategien für KI-Spieler implementieren.

## Funktionen

### `kiPlayerNumbers(hand, topCard)`

Ermittelt den Spielzug für einen KI-Spieler mit einer Strategie basierend auf den Zahlenwerten der Karten.

#### Parameter

- `hand` (list): Die Liste der Karten in der Hand.
- `topCard` (dict): Die oberste Karte.

#### Rückgabewert

- `dict`: Die Payload, die den gewählten Spielzug repräsentiert.

### `kiPlayerAll(hand, topCard, lastTopCard)`

Ermittelt den Spielzug für einen KI-Spieler mit einer Strategie, alle Karten zu verwenden.

#### Parameter

- `hand` (list): Die Liste der Karten in der Hand.
- `topCard` (dict): Die oberste Karte.
- `lastTopCard` (dict): Die letzte oberste Karte.

#### Rückgabewert

- `dict`: Die Payload, die den gewählten Spielzug repräsentiert.

### `calculate_move_utility(move, top_card_value)`

Berechnet den Nutzenwert eines Spielzugs basierend auf dem Zahlenwert der obersten Karte.

#### Parameter

- `move` (list): Der Spielzug, für den der Nutzenwert berechnet werden soll.
- `top_card_value` (int): Der Zahlenwert der obersten Karte.

#### Rückgabewert

- `int`: Der Nutzenwert des Spielzugs.

### `calculate_card_utility(value, utility_value)`

Berechnet den Nutzenwert einer Karte basierend auf ihrem Zahlenwert.

#### Parameter

- `value` (int): Der Zahlenwert der Karte.
- `utility_value` (int): Der aktuelle Nutzenwert.

#### Rückgabewert

- `int`: Der aktualisierte Nutzenwert.

### `get_best_move(possibleSets, topCard)`

Ermittelt den besten Spielzug aus einer Liste möglicher Kartensätze.

#### Parameter

- `possibleSets` (list): Die Liste möglicher Kartensätze.
- `topCard` (dict): Die oberste Karte.

#### Rückgabewert

- `tuple`: Der beste Spielzug und der Grund für seine Auswahl.

### `take()`

Führt den Spielzug "take" aus.

#### Rückgabewert

- `tuple`: Der Spielzug "take" und der Grund für seine Auswahl.

### `choose_card(hand)`

Wählt eine Karte aus der Hand basierend auf dem Nutzenwert des Spielzugs aus.

#### Parameter

- `hand` (list): Die Liste der Karten in der Hand.

#### Rückgabewert

- `tuple`: Die ausgewählte Karte und der Grund für ihre Auswahl.



Um zum Hauptmenü zurückzukehren, klicken Sie [hier](main_menu.md).
