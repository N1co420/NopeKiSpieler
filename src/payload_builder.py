

def buildPayload(move_type, reason, cards=None):
    """
    Build a payload dictionary for a move.

    :param move_type: The type of move.
    :param reason: The reason for the move.
    :param cards: The cards associated with the move. (Optional)

    :return: The payload dictionary.
    """
    payload = {
        "type": move_type,
        "card1": None,
        "card2": None,
        "card3": None,
        "reason" : reason
    }
    
    if move_type == "put":
        payload["type"] = "put"
        for i in range(len(cards)):
            card_payload = create_card_payload(cards[i])
            payload[f"card{i + 1}"] = card_payload
    elif move_type == "take":
        payload["type"] = "take"
    elif move_type == "nope":
        payload["type"] = "nope"

    payload["reason"] = reason
    
    return payload

    
def create_card_payload(card):
    """
    Create a payload dictionary for a card.

    :param card: The card information.
    
    :return: The card payload dictionary.
    """
    return {
            "type": card["type"],
            "color": card["color"],
            "value": card["value"]
    }
    
