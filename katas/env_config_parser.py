
def parse_env_config(env_string: str):
    """
    Parses environment variables string into a configuration dictionary.
    
    Parse rules:
    - Each line contains KEY=VALUE pairs
    - Ignore empty lines and comments (lines starting with #)
    - Convert numeric strings to integers
    - Convert "true"/"false" strings to booleans (case-insensitive)
    - Remove quotes from values if present
    - Handle values with spaces
    
    Example input:
    DATABASE_URL=postgres://localhost:5432/mydb
    DEBUG=true
    PORT=8080
    # This is a comment
    APP_NAME="My Application"
    MAX_CONNECTIONS=100
    
    Expected output:
    {
        "DATABASE_URL": "postgres://localhost:5432/mydb",
        "DEBUG": True,
        "PORT": 8080,
        "APP_NAME": "My Application", 
        "MAX_CONNECTIONS": 100
    }
    
    Args:
        env_string: Multi-line string containing environment variables
        
    Returns:
        Dictionary with parsed configuration values
    """
    config = {}
    lines = env_string.strip().splitlines()

    for line in lines:
        line = line.strip()
        if not line or line.startswith("#"):
            continue  # Skip empty lines and comments

        if "=" not in line:
            continue  # Skip malformed lines

        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip()
        
        if not key:
            continue  # Skip lines with empty keys

        # Remove surrounding quotes if present
        if (value.startswith('"') and value.endswith('"')) or \
           (value.startswith("'") and value.endswith("'")):
            value = value[1:-1]

        # Convert value to appropriate type
        lowered = value.lower()
        if lowered == "true":
            value = True
        elif lowered == "false":
            value = False
        elif value.isdigit():
            value = int(value)
        else:
            # Try converting negative numbers or numeric strings that include decimals
            try:
                int_val = int(value)
                value = int_val
            except ValueError:
                pass  # leave as string if not an int

        config[key] = value

    return config




if __name__ == "__main__":
    sample_env = """
# Database Configuration
DATABASE_URL=postgresql://user:pass@localhost:5432/appdb
DATABASE_POOL_SIZE=10

# Application Settings  
APP_NAME="E-Commerce API"
DEBUG=false
PORT=3000
WORKERS=4

# Feature Flags
ENABLE_LOGGING=true
ENABLE_CACHE="false"
CACHE_TTL=3600

# Empty line above should be ignored
REDIS_URL=redis://localhost:6379/0
"""
    
    config = parse_env_config(sample_env)
    print("Parsed Configuration:")
    for key, value in config.items():
        print(f"  {key}: {value} ({type(value).__name__})") 