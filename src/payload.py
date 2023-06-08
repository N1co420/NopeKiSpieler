import socketConnect
from events import *

def buildPayload(move_type, cards, reason):
    payload = {
        "type": move_type,
        "card1": None,
        "card2": None,
        "card3": None,
        "reason" : "A"
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
    if card["type"] == "number":
        return {
            "type": card["type"],
            "color": card["color"],
            "value": card["value"]
        }
    


# Do stuff for action cards



