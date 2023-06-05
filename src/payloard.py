import socketConnect
from events import *

def buildPayload(move_type, cards, select_color):
    payload = {
        "type": move_type,
        "card1": None,
        "card2": None,
        "card3": None
    }
    
    if move_type == "put":
        payload["type"] = "put"
        for i in range(len(cards)):
            card_payload = create_number_card_payload(cards[i])
            payload[f"card{i + 1}"] = card_payload
    elif move_type == "take":
        payload["type"] = "take"
    elif move_type == "nope":
        payload["type"] = "nope"
    elif move_type == "selection":
        if cards and len(cards) > 0:
            payload["card1"] = create_selection_card_payload(cards[0], select_color)

    
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

def send_payload(payload):

    response = sio.emit("game:makeMove",payload)
    # Check response status code
    if response.status_code == 200:
        print("Payload sent successfully!\n")
    else:
        print("Failed to send payload. Error:\n", response.text)

