def decide(analysis):
    if analysis["confidence"] > 0.7:
        return {
            "escalate": True,
            "action": analysis["recommended_action"]
        }

    return {
        "escalate": False,
        "action": "Wait for more data"
    }
