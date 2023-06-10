import game_rules_numbercards
from itertools import combinations

def cardOfChoice(hand):
    print("get Card of choice")
    print("bei Neustart und Joker")

def seeThough():
    print("TopCard = LastTopCard")
    print("Call KI again")

def doubleSeeThrough():
    print("use 2 Cards down")

def getJokers(hand):
    jokers = []

    for card in hand:
        cardType = card["type"]
        if cardType == "joker":
            jokers.append(card)

    return jokers

def matchingColor(cardColor, topCardColor):
    cardColors = cardColor.split('-')
    topCardColors = topCardColor.split('-')

    for color in cardColors:
        if color in topCardColors or color == "multi":
            return True

    return False

def getMatchingCards(hand, topCard):
    jokers = getJokers(hand)

    matchingCards = game_rules_numbercards.get_matching_cards(hand, topCard)

    matchingCards.extend(jokers)

    return matchingCards

def get_possible_sets(matchingCards, topCard):
    
    matchingSets = game_rules_numbercards.get_possible_number_sets(matchingCards, topCard)

    if matchingSets == None:
        matchingJokerSets = jokerCanFillSet(matchingCards, topCard)
        return matchingJokerSets
    else:
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


def bestJokerSet(sets):

    return sets[0]


    


    


