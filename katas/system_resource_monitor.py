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
    # Get overall CPU usage (with a small interval for accuracy)
    overall_usage = psutil.cpu_percent(interval=0.1)
    
    # Get number of CPU cores
    core_count = psutil.cpu_count()
    
    # Get per-core CPU usage
    per_core = psutil.cpu_percent(interval=0.1, percpu=True)
    
    return {
        'usage_percent': overall_usage,
        'core_count': core_count,
        'per_core_usage': per_core
    }


def get_memory_usage():
    """
    Gets current memory usage information.
    
    Returns:
        Dictionary with:
        - 'total_gb': Total memory in GB
        - 'available_gb': Available memory in GB
        - 'used_gb': Used memory in GB
    """
    # Get memory information
    memory = psutil.virtual_memory()
    
    # Convert bytes to GB (1 GB = 1024^3 bytes)
    gb_factor = 1024 ** 3
    
    return {
        'total_gb': round(memory.total / gb_factor, 2),
        'available_gb': round(memory.available / gb_factor, 2),
        'used_gb': round((memory.total - memory.available) / gb_factor, 2)
    }

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
    # Get disk usage information
    disk = psutil.disk_usage(path)
    
    # Convert bytes to GB
    gb_factor = 1024 ** 3
    
    return {
        'total_gb': round(disk.total / gb_factor, 2),
        'used_gb': round(disk.used / gb_factor, 2),
        'free_gb': round(disk.free / gb_factor, 2),
        'usage_percent': disk.percent
    }



if __name__ == '__main__':
    cpu_info = get_cpu_usage()
    print(f"CPU Usage: {cpu_info}")

    memory_info = get_memory_usage()
    print(f"Memory Usage: {memory_info}")

    disk_info = get_disk_usage()
    print(f"Disk Usage: {disk_info}")


