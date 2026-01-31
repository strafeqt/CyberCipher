def reason(context):
    tickets = context["tickets"]
    errors = context["errors"]

    if len(tickets) >= 2 and errors:
        return {
            "hypothesis": "Migration caused payment API auth failure",
            "confidence": 0.8,
            "root_cause": "migration_misconfiguration",
            "recommended_action": "Alert merchants to update API keys"
        }

    return {
        "hypothesis": "Unknown issue",
        "confidence": 0.3,
        "root_cause": "unknown",
        "recommended_action": "Investigate manually"
    }
