import os

def check_required_env_keys():
    """Checks for the presence of required environment variables."""
    required_keys = ["GOOGLE_API_KEY", "GOOGLE_SEARCH_ENGINE_ID"]
    missing_keys = []
    for key in required_keys:
        if not os.getenv(key):
            missing_keys.append(key)
    
    if missing_keys:
        raise EnvironmentError(f"Missing required environment variables: {', '.join(missing_keys)}. Please add them to your .env.local file.")
    else:
        print("✅ All required Google API environment variables are set.")

if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv() # Load .env.local if it exists
    check_required_env_keys()
