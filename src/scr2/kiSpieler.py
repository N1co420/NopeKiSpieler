import game_rules_numbercards
import payload_builder

def kiPlayerNumbers(hand, topCard):
    global lastTake

    matching_cards = game_rules_numbercards.get_matching_cards(hand, topCard)
    if matching_cards is None:
        lastTake = "take"
        payload = payload_builder.buildPayload(lastTake, None, "No Cards to put")
    else:
        possible_sets = game_rules_numbercards.get_possible_sets(matching_cards, topCard)

        if possible_sets is None:
            if lastTake == "take":
                lastTake = "nope"
                payload = payload_builder.buildPayload(lastTake, None, "Nope!")
            else:
                lastTake = "take"
                payload = payload_builder.buildPayload(lastTake, None, "No Cards to put")
        else:
            lastTake = "put"
            best_set = game_rules_numbercards.get_best_set(possible_sets)
            payload = payload_builder.buildPayload(lastTake, best_set, "Best Values, best Colors")

    return payload

def main():
    hand = [
        {"type": "number", "color": "blue", "value": 2},
        {"type": "number", "color": "yellow", "value": 1},
        {"type": "number", "color": "red-blue", "value": 2},
        {"type": "number", "color": "red-blue", "value": 1},
        {"type": "number", "color": "blue-green", "value": 3},
        {"type": "number", "color": "red-green", "value": 3},
        {"type": "number", "color": "red", "value": 1},
        {"type": "number", "color": "yellow-green", "value": 1}
    ]     
    
    topCard = {"type": "number", "color": "yellow", "value": 3}
    
    payload = kiPlayerNumbers(hand, topCard)

    hand2 = [
        {"type": "number", "color": "blue", "value": 2},
        {"type": "number", "color": "yellow", "value": 1},
        {"type": "number", "color": "red-blue", "value": 2},
        {"type": "number", "color": "red-blue", "value": 1},
        {"type": "number", "color": "blue-green", "value": 3},
        {"type": "number", "color": "red-green", "value": 3},
        {"type": "number", "color": "red", "value": 1},
        {"type": "number", "color": "yellow-green", "value": 1},
        {"type": "number", "color": "red", "value": 1}
    ]    
    
    topCard2 = {"type": "number", "color": "yellow", "value": 3}

    payload2 = kiPlayerNumbers(hand2, topCard2)

# Call the main function
main()