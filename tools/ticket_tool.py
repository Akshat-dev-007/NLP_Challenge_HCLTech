# tools/ticket_tool.py
def create_ticket(issue, priority):
    return {
        "type": "action_result",
        "ticket_id": "IT-2045",
        "status": "Created",
        "issue": issue,
        "priority": priority
    }
