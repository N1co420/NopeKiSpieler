import socketio
import json
import socketConnect


def myTurn(playerID, currentPlayerID):
    return playerID == currentPlayerID

def matchingColor(cardColor, topCardColor):
    return cardColor == topCardColor or cardColor == "multi"

def splitColor(cardColor):
    return cardColor.split('-')

def needsSplit(cardColor):
    split_colors = ["red-yellow", "blue-green", "yellow-blue", "red-blue", "red-green", "yellow-green"]
    return cardColor in split_colors

def getWorstCard(selection):
    worstCard = None
    highestValue = -1
    
    for card in selection:
        if card['value'] > highestValue:
            highestValue = card['value']
            worstCard = card
    
    return worstCard


def makeMove(hand, topCard, lastTopCard):
    topCardType = topCard['type']
    
    if topCardType == "number":
        validMoves = getValidMoves(hand, topCard)
        # get Best of Valid Moves
        # do Move
        return
    
    if topCardType == "joker":
        card2play = getWorstCard(hand)
        return
    
    if topCardType == "reboot":
        card2play = getWorstCard(hand)
        return
    
    if topCardType == "see-through":
        validMoves = getValidMoves(hand, lastTopCard)
        return
    
    if topCardType == "selection":
        # kläre was hier zu tun ist
        return
    
    # Handle default case or raise an exception for unsupported topCardValue
    raise ValueError("Invalid topCardValue")

def getValidMoves(hand, topCard):

    topCardValue = topCard['value']
    topCardColor = topCard['color']
    validMoves= []

    if needsSplit(topCardColor):
        color1, color2 = splitColor(topCardColor)
        matchingCards1 = [card for card in hand if matchingColor(card['color'], color1)]
        matchingCards2 = [card for card in hand if matchingColor(card['color'], color2)]
        if len(matchingCards1) >= topCardValue:
            validMoves.extend(matchingCards1)
        if len(matchingCards2) >= topCardValue:
            validMoves.extend(matchingCards2)
    else:
        matchingCards = [card for card in hand if matchingColor(card['color'], topCardColor)]
        if len(matchingCards) >= topCardValue:
            validMoves.extend(matchingCards)

    return validMoves

def move(move_type, cards, select_color):
    payload = {
        "type": move_type,
        "card1": None,
        "card2": None,
        "card3": None
    }
    
    if move_type == "put":
        # construct put payload
        print("platzhalter")
    elif move_type == "take":
        payload["type"] = "take"
    elif move_type == "nope":
        payload["type"] = "nope"
    elif move_type == "selection":
        if cards and len(cards) > 0:
            payload["card1"] = create_selection_card_payload(cards[0], select_color)

        
    # Send the payload to the server
    # Your code here to send the payload to the server
    
def create_number_card_payload(card):
    return {
        "type": "number",
        "color": card["color"],
        "value": card["value"]
    }

def create_selection_card_payload(card, select_color):
    return {
        "type": "selection",
        "color": "multi",
        "selectValue": 1,
        "selectColor": select_color
    }




