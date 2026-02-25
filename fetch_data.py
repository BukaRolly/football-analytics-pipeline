import requests
import os
from dotenv import load_dotenv

load_dotenv()
token = os.environ["FOOTBALL_API_TOKEN"]

def fetch_matches_api():
    """Fetch PL matches from football-data API."""
    url = "https://api.football-data.org/v4/competitions/PL/matches"
    headers = {"X-Auth-Token": token}
    params = {"season": 2025}

    r = requests.get(url, headers=headers, params=params)
    r.raise_for_status()  # optional: fail if API returns error
    return r.json()