import os
from dotenv import load_dotenv

def fix_environment_consistency():
    """Checks for Google API keys and prompts the user if missing."""
    load_dotenv() # Load .env.local

    google_api_key = os.getenv("GOOGLE_API_KEY")
    google_search_engine_id = os.getenv("GOOGLE_SEARCH_ENGINE_ID")

    if not google_api_key or not google_search_engine_id:
        print("\n⚠️  Warning: Google Search API credentials are missing or incomplete.")
        print("   To enable Google Search indexing pre-check, please add the following to your .env.local file:")
        print("\n   GOOGLE_API_KEY=AIzaSyBUoKsadoS-b20IDgHbkkQVkTGARGihy4U")
        print("   GOOGLE_SEARCH_ENGINE_ID=30f4bf488c4ce4130")
        print("\n   After adding, restart your application.")
    else:
        print("✅ Google Search API credentials are set.")

if __name__ == "__main__":
    fix_environment_consistency()
