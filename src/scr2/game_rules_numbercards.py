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

def get_possible_number_sets(matchingCards, topCard):
    setSize = topCard["value"]
    possibleSets = []

    for combination in combinations(matchingCards, setSize):
        setContainsOnlyNumbers = all(card["type"] == "number" for card in combination)
        if setContainsOnlyNumbers:
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





