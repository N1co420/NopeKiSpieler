from itertools import combinations
def matchingColor(cardColor, topCardColor):
    cardColors = cardColor.split('-')
    topCardColors = topCardColor.split('-')

    for color in cardColors:
        if color in topCardColors or color == "multi":
            return True

    return False

def matchingColor(cardColor, topCardColor):
    cardColors = cardColor.split('-')
    for color in cardColors:
        if color == topCardColor or color =="multi":
            return True
    return False

def get_matching_cards(hand, topCard, only_action_cards=False):
    matching_cards = []
    top_card_colors = topCard["color"].split('-')

    for color in top_card_colors:
        color_matching_cards = []
        for card in hand:
            card_color = card["color"]
            if (
                card["type"] in ["number", "joker"]
                and matchingColor(card_color, color)
                and (not only_action_cards or card["type"] not in ["number", "joker"])
            ):
                color_matching_cards.append(card)
                
        if color_matching_cards:
            matching_cards.append(color_matching_cards)

    if matching_cards:
        return matching_cards
    else:
        return None

def get_possible_sets(matchingCardsList, topCard):
    set_size = topCard["value"]
    topCardColors = topCard["color"].split('-')
    possibleSets = []

    for matchingCards in matchingCardsList:
        card_combinations = list(combinations(matchingCards, set_size))
        for combination in card_combinations:
            if combination not in possibleSets:
                possibleSets.append(list(combination))

    return possibleSets

    

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
        {"type": "number", "color": "yellow", "value": 2},
        {"type": "number", "color": "yellow-blue", "value": None},
        {"type": "number", "color": "red-blue", "value": 2},
        {"type": "see-through", "color": "yellow", "value": None},
        {"type": "number", "color": "blue-green", "value": 3},
        {"type": "number", "color": "red", "value": 1},
        {"type": "joker", "color": "multi", "value": 1},
        {"type": "number", "color": "red-green", "value": 1}
    ]     
    
    topCard = {"type": "number", "color": "yellow-blue", "value": 2}
    lastTopCard = {"type": "number", "color": "blue", "value": 3}

    moves = get_moves(hand, topCard)

    for move in moves:
        print(move)
        print(" ")
    
testing()

    
