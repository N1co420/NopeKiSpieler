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

    for combination in combinations(matchingCards, setSize):
        setsWithJoker = all((card["type"] == "number" or card["type"] == "joker") for card in combination)
        if setsWithJoker:
            possibleSets.append(list(combination))

    if len(possibleSets) > 0:
        return possibleSets
    else:
        return None



    


    


