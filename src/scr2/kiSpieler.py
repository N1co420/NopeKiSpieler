import game_rules_numbercards
import game_rules_specials
import payload_builder

lastTake = None

def kiPlayerNumbers(hand, topCard):
    global lastTake   

    matching_cards = game_rules_specials.getMatchingCards(hand, topCard)

    print("matching cards:  ")
    print(matching_cards)
    print("")
    
    if matching_cards is None:
        lastTake = "take"
        payload = payload_builder.buildPayload(lastTake, None, "No Cards to put")
    else:
        possible_sets = game_rules_specials.get_possible_sets(matching_cards, topCard)
        print("possible sets: ")
        print(possible_sets)
        print(" ")
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
        {"type": "number", "color": "green", "value": 2},
        {"type": "restart", "color": "yellow", "value": None},
        {"type": "number", "color": "red-blue", "value": 2},
        {"type": "see-through", "color": "yellow", "value": None},
        {"type": "number", "color": "blue-green", "value": 3},
        {"type": "number", "color": "red", "value": 1},
        {"type": "joker", "color": "multi", "value": 1},
        {"type": "number", "color": "yellow-green", "value": 1}
    ]     
    
    topCard = {"type": "number", "color": "red-blue", "value": 3}
    
    payload = kiPlayerNumbers(hand, topCard)
    


# Call the main function
main()