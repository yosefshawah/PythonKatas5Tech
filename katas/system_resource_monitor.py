import psutil
import subprocess
import os
from typing import Dict, List, Optional
import json
from datetime import datetime

# Note
# The unittest for this kata *must mock* the psutil and os methods to avoid actual system calls

    
def get_cpu_usage():
    """
    Gets current CPU usage information.
    
    Returns:
        Dictionary with:
        - 'usage_percent': Overall CPU usage percentage
        - 'core_count': Number of CPU cores
        - 'per_core_usage': List of per-core usage percentages
    """
    # TODO: Use psutil to get CPU information, e.g. psutil.cpu_percent() for overall usage
    pass


def get_memory_usage():
    """
    Gets current memory usage information.
    
    Returns:
        Dictionary with:
        - 'total_gb': Total memory in GB
        - 'available_gb': Available memory in GB
        - 'used_gb': Used memory in GB
    """
    # TODO: Use psutil.virtual_memory()
    pass

def get_disk_usage(path: str = "/") -> Dict:
    """
    Gets disk usage for specified path.
    
    Args:
        path: Disk path to check (default: root)
        
    Returns:
        Dictionary with:
        - 'total_gb': Total disk space in GB
        - 'used_gb': Used disk space in GB
        - 'free_gb': Free disk space in GB
        - 'usage_percent': Disk usage percentage
    """
    # TODO: Use psutil.disk_usage(path)
    # Convert bytes to GB
    pass



if __name__ == '__main__':
    cpu_info = get_cpu_usage()
    print(f"CPU Usage: {cpu_info}")

    memory_info = get_memory_usage()
    print(f"Memory Usage: {memory_info}")

    disk_info = get_disk_usage()
    print(f"Disk Usage: {disk_info}")


