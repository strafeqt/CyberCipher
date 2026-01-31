import json

def load_events():
    with open("data/mock_events.json") as f:
        return json.load(f)

def observe():
    events = load_events()

    tickets = [e for e in events if e["type"] == "support_ticket"]
    errors = [e for e in events if e["type"] == "platform_error"]

    return {
        "tickets": tickets,
        "errors": errors
    }
