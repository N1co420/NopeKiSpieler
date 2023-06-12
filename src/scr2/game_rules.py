from itertools import combinations

def matchingColor(cardColor, topCardColor):
    cardColors = cardColor.split('-')
    for color in cardColors:
        if (
            color == topCardColor 
            or color =="multi" 
            or topCardColor == "multi"
        ):
            return True
        
    return False

def get_matching_cards(hand, topCard, only_action_cards=False):
    matching_cards = []
    top_card_colors = topCard["color"].split('-')

    for color in top_card_colors:
        color_matching_cards = []
        color_matching_actioncards = []
        for card in hand:
            card_color = card["color"]
            if (
                not only_action_cards
                and card["type"] in ["number", "joker"]
                and matchingColor(card_color, color)
            ):
                color_matching_cards.append(card)
            elif (
                only_action_cards
                and card["type"] not in ["number", "joker"]
                and matchingColor(card_color, color)
            ):
                color_matching_actioncards.append(card)
                
        if color_matching_cards:
            matching_cards.append(color_matching_cards)
        elif color_matching_actioncards:
            matching_cards.append(color_matching_actioncards)

    if matching_cards:
        return matching_cards
    else:
        return None

def get_possible_sets(matchingCardsList, topCard, joker_count):
    set_size = topCard["value"]
    topCardColors = topCard["color"].split('-')
    possibleSets = []

    for matchingCards in matchingCardsList:
        card_combinations = list(combinations(matchingCards, set_size))
        for combination in card_combinations:
            if combination not in possibleSets:
                possibleSets.append(list(combination))

    if joker_count == set_size:
        joker_combination = [{"type": "joker", "color": "multi", "value": 1}] * set_size
        if joker_combination not in possibleSets:
            possibleSets.append(joker_combination)

    return possibleSets 

def get_joker_count(cards):
    joker_count = 0
    for card in cards:
        if card["type"] == "joker":
            joker_count += 1
    return joker_count

def get_moves(hand, topCard):
    moves = []
    cards = get_matching_cards(hand, topCard, only_action_cards=False)
    actionCards = get_matching_cards(hand, topCard, only_action_cards=True)
    if cards is None and actionCards is None:
        return None
    
    if cards is not None:
        jokers = get_joker_count(hand)
        setMoves = get_possible_sets(cards, topCard, jokers)
    
        if setMoves is not None:
            moves.extend([move for move in setMoves]) 
    
    if actionCards is not None:
        moves.extend([move for move in actionCards])

    if moves is None:
        return None
    return moves

def testing():
    hand = [
        {"type": "see-through", "color": "blue", "value": None},
        {"type": "number", "color": "red", "value": 2}
    ]     
    
    topCard = {"type": "number", "color": "blue-green", "value": 2}
    lastTopCard = {"type": "number", "color": "blue-green", "value": 1}
    topCardColor = topCard["color"]

    actions = get_matching_cards(hand, topCard, only_action_cards=True)

    moves = get_moves(hand, topCard)

    print(moves)# Hier ist moves leer

testing()


    
