import re


def parse_fastapi_log(log_line: str):
    """
    Parses a single FastAPI request log entry into a structured dictionary.

    Expected FastAPI log format:
    INFO:     127.0.0.1:54321 - "GET /api/users HTTP/1.1" 200 OK
    
    The parsed log data should be returned as a dictionary:
    {
        "client_ip": "127.0.0.1",
        "client_port": "54321", 
        "http_method": "GET",
        "endpoint": "/api/users",
        "http_version": "1.1",
        "status_code": "200",
        "status_text": "OK"
    }
    
    Hint: Use regex to extract each component
    
    Args:
        log_line: A single FastAPI log line string
        
    Returns:
        Dictionary with parsed log components, or empty dict if invalid format
    """
    return {}


if __name__ == "__main__":
    test_logs = [
        'INFO:     127.0.0.1:54321 - "GET /api/users HTTP/1.1" 200 OK',
        'INFO:     192.168.1.100:45678 - "POST /api/auth/login HTTP/1.1" 401 Unauthorized',
        'INFO:     10.0.0.5:33333 - "PUT /api/users/123 HTTP/1.1" 200 OK',
        'INFO:     203.0.113.25:12345 - "DELETE /api/orders/456 HTTP/1.1" 204 No Content',
        'INFO:     172.16.0.1:8080 - "GET /health HTTP/1.1" 500 Internal Server Error'
    ]
    
    print("FastAPI Log Parsing Results:")
    for i, log_line in enumerate(test_logs, 1):
        parsed = parse_fastapi_log(log_line)
        print(f"\nLog {i}:")
        print(f"  Input: {log_line}")
        print(f"  Parsed: {parsed}")
