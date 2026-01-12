from typing import Dict, Any, List

def process_user_data(user_data: Dict[str, Any], include_history: bool = False) -> Dict[str, Any]:
    user_id: int = user_data["id"]      # Extract user ID
    name: str = user_data["name"]       # Extract user name

    result: Dict[str, Any] = {
        "display_name": f"User {name}",          # Format name
        "normalized_id": str(user_id).zfill(8)   # Pad ID to 8 digits
    }

    if include_history:
        result["history"] = get_user_history(user_id)

    return result


def get_user_history(user_id: int) -> List[Dict[str, str]]:
    """
    Simulate fetching user history from a database.
    
    Args:
        user_id (int): The user's ID.
    
    Returns:
        list: A list of dictionaries representing user actions.
    """
    return [
        {"action": "login", "timestamp": "2023-10-01T10:30:00"},
        {"action": "purchase", "timestamp": "2023-10-02T14:20:00"}
    ]


# 🔹 Sample usage
if __name__ == "__main__":
    sample_user: Dict[str, Any] = {"id": 42, "name": "Alice"}
    processed = process_user_data(sample_user, include_history=True)
    print(processed)
