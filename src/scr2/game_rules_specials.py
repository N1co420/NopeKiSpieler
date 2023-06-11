import game_rules_numbercards
from itertools import combinations

def getJokers(hand):
    jokers = []

    for card in hand:
        cardType = card["type"]
        if cardType == "joker":
            jokers.append(card)

    return jokers

def getMatchingActionCards(hand, topCardColor):
    actionCards = []

    for card in hand:
        if card["type"] != "number":
            color = card["color"]
            if matchingColor(color, topCardColor):
                actionCards.append(card)

    return actionCards

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

def get_possible_sets(matchingCards, topCard):
    
    matchingSets = jokerCanFillSet(matchingCards, topCard)
    matchingActions = getMatchingActionCards(matchingCards, topCardColor=topCard["color"])

    if matchingSets == None:
        matchingJokerSets = jokerCanFillSet(matchingCards, topCard)
        matchingJokerSets.extend([matchingAction] for matchingAction in matchingActions)
        return matchingJokerSets
    else:
        matchingSets.extend([matchingAction] for matchingAction in matchingActions)
        return matchingSets

def jokerCanFillSet(matchingCards, topCard):
    setSize = topCard["value"]
    possibleSets = []

    if setSize > len(matchingCards):
        return None
    
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




    


    


