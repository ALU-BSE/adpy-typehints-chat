from typing import Dict, Any, List

def process_user_data(user_data: Dict[str, Any], include_history: bool = False) -> Dict[str, Any]:
    user_id: int = user_data["id"]      
    name: str = user_data["name"]       

    result: Dict[str, Any] = {
        "display_name": f"User {name}",          
        "normalized_id": str(user_id).zfill(8)   
    }

    if include_history:
        result["history"] = get_user_history(user_id)

    return result


def get_user_history(user_id: int) -> List[Dict[str, str]]:
    
    return [
        {"action": "login", "timestamp": "2023-10-01T10:30:00"},
        {"action": "purchase", "timestamp": "2023-10-02T14:20:00"}
    ]


# 🔹 Sample usage
if __name__ == "__main__":
    sample_user: Dict[str, Any] = {"id": 42, "name": "Alice"}
    processed = process_user_data(sample_user, include_history=True)
    print(processed)
