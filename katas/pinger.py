import subprocess
import time

# Note
# The unittest for this kata *must mock* the ping to avoid actual network calls.



def ping_host(hostname: str, count: int = 5):
    """
    Pings a host and returns connection statistics.
    
    Args:
        hostname: Host to ping (e.g., 'google.com')
        count: Number of ping attempts
        
    Returns:
        Dictionary with:
        - 'host': hostname
        - 'avg_response_time_ms': average response time in milliseconds
        - 'success': True if any packets received
    """
    # TODO: Use subprocess.run() to execute ping command
    # Linux/Mac: ping -c {count} {hostname}
    # Parse output to extract the average latency in milliseconds
    pass




if __name__ == '__main__':
    # Test the functions
    ping_result = ping_host("8.8.8.8", 3)
    print(f"Ping result: {ping_result}")
