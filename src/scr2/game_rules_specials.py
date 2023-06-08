
def cardOfChoice(hand):
    print("get Card of choice")
    print("bei Neustart und Joker")

def seeThough():
    print("TopCard = LastTopCard")
    print("Call KI again")

def matchingColor(cardColor, topCardColor):
    cardColors = cardColor.split('-')
    topCardColors = topCardColor.split('-')

    for color in cardColors:
        if color in topCardColors or color == "multi":
            return True

    return False

def get_possible_sets(matchingCards, topCard):
    print("mit Joker, See-Through and restart")