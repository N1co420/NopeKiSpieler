from itertools import combinations

def matchingColor(cardColor, topCardColor):
    """
    Checks if a card color matches the top card color or if it is a wild card.

    Parameters:
        cardColor (str): The color of the card.
        topCardColor (str): The color of the top card.

    Returns:
        bool: True if the card color matches the top card color or is a wild card, False otherwise.
    """
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
    """
    Retrieves the cards in the hand that match the color of the top card.

    Parameters:
        hand (list): The list of cards in the hand.
        topCard (dict): The top card.
        only_action_cards (bool): Optional. If True, only matching action cards will be returned.

    Returns:
        list: The list of matching cards or action cards.
    """
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
    """
    Finds all possible sets of cards that can be played based on the matching cards.

    Parameters:
        matchingCardsList (list): The list of matching cards.
        topCard (dict): The top card.
        joker_count (int): The number of joker cards in the hand.

    Returns:
        list: The list of possible sets of cards.
    """
    set_size = topCard["value"]
    topCardColors = topCard["color"].split('-')
    possibleSets = []

    for matchingCards in matchingCardsList:
        card_combinations = list(combinations(matchingCards, set_size))
        for combination in card_combinations:
            print(combination)
            if (combination not in possibleSets) :
                possibleSets.append(list(combination))

    if joker_count == set_size:
        joker_combination = [{"type": "joker", "color": "multi", "value": 1}] * set_size
        if joker_combination not in possibleSets:
            possibleSets.append(joker_combination)

    return possibleSets 

def get_joker_count(cards):
    """
    Counts the number of joker cards in the given list of cards.

    Parameters:
        cards (list): The list of cards.

    Returns:
        int: The number of joker cards.
    """
    joker_count = 0
    for card in cards:
        if card["type"] == "joker":
            joker_count += 1
    return joker_count

def get_moves(hand, topCard):
    """
    Retrieves the valid moves that can be made based on the current hand and the top card.

    Parameters:
        hand (list): The list of cards in the hand.
        topCard (dict): The top card.

    Returns:
        list: The list of valid moves.
    """
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
        for card in actionCards:
            for c in card: #Somehow this needs to be done to split the list correctly
                moves.append([c])

    if moves is None:
        return None
    return moves


