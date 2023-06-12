# game_rules.py

Die Datei `game_rules.py` enthält Funktionen, die die Regeln des Spiels implementieren und verschiedene Spielaktionen unterstützen.

## Funktionen

### `matchingColor(cardColor, topCardColor)`

Überprüft, ob die Farbe einer Karte zur Farbe der obersten Karte passt oder ob es sich um eine Joker-Karte handelt.

#### Parameter

- `cardColor` (str): Die Farbe der Karte.
- `topCardColor` (str): Die Farbe der obersten Karte.

#### Rückgabewert

- `bool`: True, wenn die Farbe der Karte zur Farbe der obersten Karte passt oder es sich um eine Joker-Karte handelt, andernfalls False.

### `get_matching_cards(hand, topCard, only_action_cards=False)`

Ruft die Karten in der Hand ab, die zur Farbe der obersten Karte passen.

#### Parameter

- `hand` (list): Die Liste der Karten in der Hand.
- `topCard` (dict): Die oberste Karte.
- `only_action_cards` (bool): Optional. Wenn True, werden nur passende Aktionskarten zurückgegeben.

#### Rückgabewert

- `list`: Die Liste der passenden Karten oder Aktionskarten.

### `get_possible_sets(matchingCardsList, topCard, joker_count)`

Ermittelt alle möglichen Kartensätze, die auf Grundlage der passenden Karten gespielt werden können.

#### Parameter

- `matchingCardsList` (list): Die Liste der passenden Karten.
- `topCard` (dict): Die oberste Karte.
- `joker_count` (int): Die Anzahl der Joker-Karten in der Hand.

#### Rückgabewert

- `list`: Die Liste der möglichen Kartensätze.


Um zum Hauptmenü zurückzukehren, klicken Sie [hier](main_menu.md).

