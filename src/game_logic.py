import socketio
import json
import socketConnect
from events import *

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

def bestMove(validMoves):
    # currently just choose the first one
    return validMoves[0]

def makeMove(hand, topCard, lastTopCard):
    topCardType = topCard['type']
    
    if topCardType == "number":
        validMoves = getValidMoves(hand, topCard)
        cards = bestMove(validMoves)
        return cards
    
    if topCardType == "joker":
        card2play = getWorstCard(hand)
        return card2play
    
    if topCardType == "reboot":
        card2play = getWorstCard(hand)
        return card2play
    
    if topCardType == "see-through":
        validMoves = getValidMoves(hand, lastTopCard)
        cards = bestMove(validMoves)
        return cards
    
    if topCardType == "selection":
        # kläre was hier zu tun ist
        return
    
    # Handle default case or raise an exception for unsupported topCardValue
    raise ValueError("Invalid topCardValue")