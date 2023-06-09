
import game_rules
import payload_builder

lastTake = None

def kiPlayerNumbers(hand, topCard): 
    """
    Determines the move for a player with a strategy based on numbers.

    Parameters:
        hand (list): The list of cards in the hand.
        topCard (dict): The top card.

    Returns:
        dict: The payload representing the chosen move.
    """
    matching_cards = game_rules.get_matching_cards(hand, topCard, only_action_cards=False)
    
    if matching_cards is None:
        payload = take()
    else:
        possible_sets = game_rules.get_moves(matching_cards, topCard)
        if possible_sets is None:
            payload = take()
        else:
            lastTake = "put"
            best_set = get_best_move(possible_sets)
            payload = payload_builder.buildPayload(lastTake, best_set, "Best Values, best Colors")

    return payload

def kiPlayerAll(hand, topCard, lastTopCard):
    """
    Determines the move for a player with a strategy to use all cards.

    Parameters:
        hand (list): The list of cards in the hand.
        topCard (dict): The top card.
        lastTopCard (dict): The last top card.

    Returns:
        dict: The payload representing the chosen move.
    """
    global lastTake
    topCardColor = topCard["color"]
    topCardValue = topCard["value"]
    topCardType = topCard["type"]

    if topCardType == "see-through":
        payload = kiPlayerAll(hand, lastTopCard, lastTopCard)
        return payload
    elif topCardType == "reboot":
        lastTake = "put"
        move, reason = choose_card(hand)
        payload = payload_builder.buildPayload(lastTake, reason, move)
        return payload
    
    moves = game_rules.get_moves(hand, topCard)
    
    if moves is None or len(moves) < 1:
        lastTake, reason = take()
        payload = payload_builder.buildPayload(lastTake, reason, None)
    else:
        lastTake = "put"
        best_move, reason = get_best_move(moves, topCard)
        payload = payload_builder.buildPayload(lastTake, reason, best_move)

    return payload

def calculate_move_utility(move, top_card_value):
    """
    Calculates the utility value of a move based on the top card value.

    Parameters:
        move (list): The move to calculate the utility value for.
        top_card_value (int): The value of the top card.

    Returns:
        int: The utility value of the move.
    """
    utility_value = 0

    for card in move:
        card_color = card["color"]
        
        if card["type"] != "number":
            utility_value = calculate_card_utility(top_card_value, utility_value)
        else:
            utility_value = calculate_card_utility(card["value"], utility_value)

        if len(card_color.split('-')) == 1 :
            utility_value *= 0.75

    return utility_value

def calculate_card_utility(value, utility_value):
    """
    Calculates the utility value of a card based on its value.

    Parameters:
        value (int): The value of the card.
        utility_value (int): The current utility value.

    Returns:
        int: The updated utility value.
    """
    if value == 1:
        utility_value -= 1
    elif value == 2:
        utility_value += 1
    else:  # value == 3
        utility_value += 2

    return utility_value

def get_best_move(possibleSets, topCard):
    """
    Determines the best move from a list of possible sets of cards.

    Parameters:
        possibleSets (list): The list of possible sets.
        topCard (dict): The top card.

    Returns:
        tuple: The best move and the reason for choosing it.
    """
    best_move = None
    bestmove_value = 100
    
    topCardValue =  topCard["value"]

    for move in possibleSets:
        move_value = calculate_move_utility(move,topCardValue)
        if move_value < bestmove_value:
            bestmove_value = move_value
            best_move = move

    reason = "Best Move utility:  ", str(move_value)
    return best_move, reason
        
def take():
    """
    Executes the "take" move.

    Returns:
        tuple: The move "take" and the reason for choosing it.
    """
    global lastTake
    reason = ""

    if lastTake == "take":
        lastTake = "nope"
        reason = "Still no cards and lastMove was Take"
    else:
        lastTake = "take"
        reason = "No Cards to put"

    return lastTake, reason


def choose_card(hand):
    """
    Chooses a card from the hand based on the move utility.

    Parameters:
        hand (list): The list of cards in the hand.

    Returns:
        tuple: The chosen card and the reason for choosing it.
    """
    chosen_card  = None
    move_utility = -100

    for card in hand:
        card_move_utility = calculate_move_utility([card], 1)
        if card_move_utility > move_utility:
            move_utility = card_move_utility
            chosen_card = [card] # has to be dict since normal moves are also dict

    chosen_reason  = "Card with best move_utility: ", str(move_utility)
    return chosen_card , chosen_reason 

def main():
    

    hand = [
        {"type": "reboot", "color": "red-green", "value": 3},
        {"type": "reboot", "color": "red-blue", "value": 2},
        {"type": "reboot", "color": "red-blue", "value": 1},
        {"type": "reboot", "color": "red-blue", "value": 1},
        {"type": "reboot", "color": "blue", "value": 2},
        {"type": "reboot", "color": "red3", "value": 3}
    ]     
    
    topCard = {"type": "number", "color": "blue", "value": 2}
    lastTopCard = {"type": "number", "color": "blue-green", "value": 1}
    topCardColor = topCard["color"]

    #sets = game_rules.get_possible_sets(list, topCard, 0)

    #moves = game_rules.get_moves(hand, topCard)
    

    move = kiPlayerAll(hand, topCard, lastTopCard)

    print(move)
# Only execute the main function if the script is run directly
if __name__ == "__main__":
    main()