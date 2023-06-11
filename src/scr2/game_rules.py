from itertools import combinations

def matchingColor(cardColor, topCardColor):
    cardColors = cardColor.split('-')
    topCardColors = topCardColor.split('-')

    for color in cardColors:
        if color in topCardColors or color == "multi":
            return True

    return False

def getMatchingCards(hand, topCard):
    matchingCards = []
    topCardColor = topCard["color"]

    for card in hand:
        color = card["color"]
        if matchingColor(color, topCardColor):
            matchingCards.append(card)

    return matchingCards

def getMatchingActionCards(hand, topCard):
    actionCards = []
    topCardColor = topCard["color"]

    for card in hand:
        if card["type"] != "number":
            color = card["color"]
            if matchingColor(color, topCardColor):
                actionCards.append(card)

    return actionCards

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
    cards = getMatchingCards(hand, topCard)
    if cards is None:
        return None
    
    moves = get_possible_sets(cards, topCard)

    actionCards = getMatchingActionCards(hand, topCard)
    
    moves.extend([[matchingAction] for matchingAction in actionCards])  
    
    if moves is None:
        return None
    
    return moves

def main():
    hand = [
        {"type": "number", "color": "yellow", "value": 2},
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

    moves = get_moves(hand, topCard)

    for move in moves:
        print(move)


