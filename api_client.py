import requests
from bs4 import BeautifulSoup
import re

BASE_URL = "https://www.cricbuzz.com"
LIVE_SCORES_URL = "https://www.cricbuzz.com/cricket-match/live-scores"

def get_matches():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    try:
        response = requests.get(LIVE_SCORES_URL, headers=headers)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return []

    soup = BeautifulSoup(response.text, "lxml")
    matches = []
    
    # Find all links that look like match links
    # Pattern: /live-cricket-scores/<id>/<slug>
    links = soup.find_all("a", href=re.compile(r"^/live-cricket-scores/\d+/"))

    seen_ids = set()

    for link in links:
        href = link.get("href")
        title = link.get("title")
        
        if not title:
            continue
            
        # Extract Match ID
        match_id_match = re.search(r"/live-cricket-scores/(\d+)/", href)
        if not match_id_match:
            continue
        
        match_id = match_id_match.group(1)
        
        if match_id in seen_ids:
            continue
        seen_ids.add(match_id)

        # Parse title for basic info
        # Format usually: "Team A vs Team B, Match Description - Status"
        # Example: "Bangladesh vs Ireland, 2nd Test - Stumps "
        
        parts = title.split(" - ")
        if len(parts) >= 2:
            name_part = parts[0]
            status = parts[-1].strip()
        else:
            name_part = title
            status = "Unknown"

        matches.append({
            "id": match_id,
            "title": name_part,
            "status": status,
            "url": BASE_URL + href,
            "description": title
        })

    return matches

if __name__ == "__main__":
    # Test the function
    matches = get_matches()
    for m in matches:
        print(f"{m['id']}: {m['title']} [{m['status']}]")
