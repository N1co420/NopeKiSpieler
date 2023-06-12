
import game_rules
import payload_builder

lastTake = None

def kiPlayerNumbers(hand, topCard): 

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
    global lastTake
    topCardColor = topCard["color"]
    topCardValue = topCard["value"]
    topCardType = topCard["type"]

    if topCardType == "see-through":
        payload = kiPlayerAll(hand, lastTopCard, lastTopCard)
        return None
    
    matchingCards = game_rules.get_matching_cards(hand, topCard,only_action_cards=False)
    
    if matchingCards is None:
        #take
        lastTake, reason = take()
        payload = payload_builder.buildPayload(lastTake, reason)
        return payload
    if topCardType != "number":
        lastTake = "put"
        # choose one card from your hand
        choosen_card, reason = choose_card(hand)
        payload = payload_builder.buildPayload(lastTake, reason, choosen_card)
    else:
        possibleSets = game_rules.get_moves(matchingCards, topCard)
        
        if possibleSets is None:
            # take
            lastTake, reason = take()
            payload = payload_builder.buildPayload(lastTake, reason)
            return payload
        else:
            lastTake = "put"
            # Choose best set and play it
            best_set, reason = get_best_move(possibleSets, topCard)
            payload = payload_builder.buildPayload(lastTake, reason, best_set)
    return payload

def calculate_move_utility(move, top_card_value):
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
    if value == 1:
        utility_value -= 1
    elif value == 2:
        utility_value += 1
    else:  # value == 3
        utility_value += 2

    return utility_value

def get_best_move(possibleSets, topCard):
    best_move = None
    bestmove_value = 100
    reason = "Fuck you"
    topCardValue =  topCard["value"]

    for move in possibleSets:
        move_value = calculate_move_utility(move,topCardValue)
        if move_value < bestmove_value:
            bestmove_value = move_value
            best_move = move

    return best_move, reason
        
def take():
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

    chosen_card  = None
    move_utility = -100

    for card in hand:
        card_move_utility = calculate_move_utility([card], 1)
        if card_move_utility > move_utility:
            move_utility = card_move_utility
            chosen_card = [card] # has to be dict since normal moves are also dict

    chosen_reason  = "Card with best move_utility: "+ str(move_utility)
    return chosen_card , chosen_reason 

def main():
    

    hand = [
        {"type": "see-through", "color": "yellow-green", "value": 2},
        {"type": "number", "color": "red-green", "value": 3},
        {"type": "number", "color": "blue-green", "value": 2},
        {"type": "number", "color": "red-green", "value": 2},
        {"type": "number", "color": "yellow-blue", "value": 2},
        {"type": "restart", "color": "red", "value": 3},
        {"type": "joker", "color": "multi", "value": 1},
        {"type": "number", "color": "green", "value": 2}
    ]     
    
    topCard = {"type": "number", "color": "red-yellow", "value": 2}
    lastTopCard = {"type": "number", "color": "blue", "value": 3}
    
    moves = game_rules.get_moves(hand, topCard)
    
    
# Only execute the main function if the script is run directly
if __name__ == "__main__":
    main()