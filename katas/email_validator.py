import re


def is_valid_email(email: str):
    """
    Validates if an email address is properly formatted.
    
    Basic email validation rules:
    - Must contain exactly one @ symbol
    - Must have a local part before @ (1-64 characters)
    - Must have a domain part after @ (1-253 characters)
    - Domain must be REAL (hint: check it in python by os.gethostbyname())
    - Local part can contain letters, numbers, and some special chars: . _ % + -
    - Must not start or end with special characters
    
    You must use regex pattern matching
    
    Args:
        email: The email string to validate
        
    Returns:
        True if the email is valid, False otherwise
    """
    return False


if __name__ == "__main__":
    test_emails = [
        "user@cnn.com",           # Valid
        "john.doe@cnn.com",     # Valid
        "admin+test@cnn.com",        # Valid
        "user_name@cnn.com",  # Valid
        "user@@domain",           # Invalid 
        "",                           # Invalid - empty
        "user@domain..com",           # Invalid - double dot
    ]
    
    for email in test_emails:
        result = is_valid_email(email)
        print(f"'{email}' is valid: {result}") 