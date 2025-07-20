import json
from typing import Dict, List, Any, Optional


def extract_user_data(api_response: str) -> List[Dict[str, str]]:
    """
    Extracts and formats user data from a REST API response.
    
    The API response contains a list of users with nested data.
    Extract only the essential information for each user:
    - id (string)
    - name (string) 
    - email (string)
    - company_name (string from nested company object)
    - city (string from nested address object)
    
    Handle missing or null fields gracefully by using "Unknown" as default.
    
    Args:
        api_response: JSON string from API containing user data
        
    Returns:
        List of dictionaries with extracted user information
        
    Raises:
        ValueError: if the JSON is invalid
    """
    # result should ne of this format: [{id: "1",... }, {},]
    
    data = json.loads(api_response)
    res = []
    for user in data.get("users", []):
        company = user.get("company") or {}
        address = user.get("address") or {}
        
        res.append({
            "id": user.get("id") or "Unknown",
            "name": user.get("name") or "Unknown" ,
            "email": user.get("email") or "Unknown",
            "company_name": company.get("name") or "Unknown",
            "city": address.get("city") or "Unknown"
        })  
    return res

if __name__ == "__main__":
    sample_response = '''
    {
      "users": [
        {
          "id": "1",
          "name": "John Doe",
          "email": "john@example.com",
          "company": {
            "name": "Tech Corp",
            "website": "techcorp.com"
          },
          "address": {
            "city": "New York",
            "zipcode": "10001"
          }
        },
        {
          "id": "2", 
          "name": "Jane Smith",
          "email": "jane@company.org",
          "company": {
            "name": "Innovation Ltd"
          },
          "address": {
            "city": "San Francisco"
          }
        },
        {
          "id": "3",
          "name": "Bob Wilson", 
          "email": null,
          "company": null,
          "address": {
            "city": "Boston"
          }
        }
      ]
    }
    '''
    
    users = extract_user_data(sample_response)
    print("Extracted User Data:")
    for user in users:
        print(f"  ID: {user['id']}, Name: {user['name']}, Email: {user['email']}")
        print(f"    Company: {user['company_name']}, City: {user['city']}") 