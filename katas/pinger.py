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
    try:
        # Run ping command and capture output
        result = subprocess.run(
            ['ping', '-c', str(count), hostname],
            capture_output=True,
            text=True,
            check=False
        )
        
        # Initialize response dictionary
        response = {
            'host': hostname,
            'avg_response_time_ms': 0.0,
            'success': False
        }
        
        # Check if ping was successful
        if result.returncode == 0:
            # Extract average time from output
            output_lines = result.stdout.split('\n')
            for line in output_lines:
                if 'avg' in line:
                    # Format: round-trip min/avg/max/stddev = 10.123/15.456/20.789/2.345 ms
                    stats = line.split('=')[1].strip().split('/')
                    response['avg_response_time_ms'] = float(stats[1])
                    response['success'] = True
                    break
        
        return response
    except Exception as e:
        return {
            'host': hostname,
            'avg_response_time_ms': 0.0,
            'success': False
        }




if __name__ == '__main__':
    # Test the functions
    ping_result = ping_host("8.8.8.8", 3)
    print(f"Ping result: {ping_result}")
