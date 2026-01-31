def act(decision):
    if decision["escalate"]:
        return f"PROPOSED ACTION: {decision['action']} (needs approval)"
    else:
        return "No action yet"
