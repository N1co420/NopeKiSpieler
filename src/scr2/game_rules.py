from itertools import combinations

def matchingColor(cardColor, topCardColor):
    cardColors = cardColor.split('-')
    topCardColors = topCardColor.split('-')

    for color in cardColors:
        if color in topCardColors or color == "multi":
            return True

    return False

def get_matching_cards(hand, topCard, only_action_cards=False):
    matching_cards = []
    top_card_color = topCard["color"]

    for card in hand:
        color = card["color"]
        if matchingColor(color, top_card_color) and (not only_action_cards or card["type"] != "number"):
            matching_cards.append(card)

    return matching_cards

def get_possible_sets(matchingCards, topCard):
    setSize = topCard["value"]
    possibleSets = []

    Cards = [card for card in matchingCards if card["type"] == "number" or card["type"] == "joker"]
    cardsCombination = combinations(Cards, setSize)

    for combination in cardsCombination:
        colorsMatch = True
        for card1 in combination:
            for card2 in combination:
                if card1 != card2:
                    if not matchingColor(card1["color"], card2["color"]) and not card1["type"] == "joker" and not card2["type"] == "joker":
                        colorsMatch = False
                        break
            if not colorsMatch:
                break
        if colorsMatch:
            possibleSets.append(list(combination))          

    if len(possibleSets) > 0:
        return possibleSets
    else:
        return None

def get_moves(hand, topCard):
    moves = []
    cards = get_matching_cards(hand, topCard, only_action_cards=False)
    if cards is None:
        return None
    
    setMoves = get_possible_sets(cards, topCard)
    if setMoves is not None:
        moves.extend([move for move in setMoves])

    actionCards = get_matching_cards(hand, topCard, only_action_cards=True)
    if actionCards is not None:
        moves.extend([[matchingAction] for matchingAction in actionCards])  
    
    if moves is None or len(moves) < topCard["value"]:
        return None
    return moves

def testing():
    hand = [
        {"type": "number", "color": "green", "value": 2},
        {"type": "restart", "color": "red-blue", "value": None},
        {"type": "number", "color": "red-blue", "value": 2},
        {"type": "see-through", "color": "red", "value": None},
        {"type": "number", "color": "blue-green", "value": 3},
        {"type": "number", "color": "red", "value": 1},
        {"type": "joker", "color": "multi", "value": 1},
        {"type": "number", "color": "red-green", "value": 1}
    ]     
    
    topCard = {"type": "number", "color": "yellow", "value": 2}
    lastTopCard = {"type": "number", "color": "blue", "value": 3}

    cards = get_matching_cards(hand, topCard, only_action_cards=False)
    moves = get_moves(cards, topCard)

    
