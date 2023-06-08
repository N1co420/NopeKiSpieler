from itertools import combinations
import payload_builder

lastTake = None

def matchingColor(cardColor, topCardColor):
    cardColors = cardColor.split('-')
    topCardColors = topCardColor.split('-')

    for color in cardColors:
        if color in topCardColors:
            return True

    return False

def get_matching_cards(hand, topCard):
    topCardColor = topCard["color"]
    matchingCards = []
    
    for card in hand:
        cardColor = card["color"]
        if matchingColor(cardColor, topCardColor):
            matchingCards.append(card)
    
    if len(matchingCards) > 0:
        return matchingCards
    else:
        return None

def get_possible_sets(matchingCards, topCard):
    setSize = topCard["value"]
    possibleSets = []

    for combination in combinations(matchingCards, setSize):
        possibleSets.append(list(combination))

    if len(possibleSets) > 0:
        return possibleSets
    else:
        return None

def get_best_set(possibleSets):
    best_set = None
    highest_last_value = float('-inf')
    lowest_values = float('inf')
    best_set_size = float('inf')

    for set_cards in possibleSets:
        last_value = set_cards[-1]['value']
        values = [card['value'] for card in set_cards[:-1]]
        total_value = sum(values)
        set_size = len(set_cards)

        if last_value > highest_last_value:
            best_set = set_cards
            highest_last_value = last_value
            lowest_values = total_value
            best_set_size = set_size
        elif last_value == highest_last_value:
            if set_size < best_set_size:
                best_set = set_cards
                lowest_values = total_value
                best_set_size = set_size
            elif set_size == best_set_size and total_value < lowest_values:
                best_set = set_cards
                lowest_values = total_value

    return best_set

def kiPlayerNumbers(hand, topCard):
    global lastTake

    matching_cards = get_matching_cards(hand, topCard)
    if matching_cards is None:
        lastTake = "take"
        payload = payload_builder.buildPayload(lastTake, None, "No Cards to put")
    else:
        possible_sets = get_possible_sets(matching_cards, topCard)

        if possible_sets is None:
            if lastTake == "take":
                lastTake = "nope"
                payload = payload_builder.buildPayload(lastTake, None, "Nope!")
            else:
                lastTake = "take"
                payload = payload_builder.buildPayload(lastTake, None, "No Cards to put")
        else:
            lastTake = "put"
            best_set = get_best_set(possible_sets)
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



