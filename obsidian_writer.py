import os
import re
from datetime import datetime

def sanitize_filename(name):
    # Remove invalid characters for filenames
    return re.sub(r'[<>:"/\\|?*]', '', name).strip()

def create_match_note(vault_path, match_data):
    """
    Creates a markdown file in the Obsidian vault for the given match.
    """
    if not os.path.exists(vault_path):
        os.makedirs(vault_path, exist_ok=True)

    # Parse title to get team names if possible
    # Title format: "Team A vs Team B, Match Description"
    title = match_data['title']
    teams = []
    if " vs " in title:
        teams_part = title.split(",")[0]
        teams = teams_part.split(" vs ")
    
    today = datetime.now().strftime("%Y-%m-%d")
    filename = f"{today} - {sanitize_filename(teams_part if teams else title)}.md"
    file_path = os.path.join(vault_path, filename)

    # Generate ESPNcricinfo search link
    # We don't have the direct link, but a search link is a good fallback
    # Format: https://www.espncricinfo.com/search?q=Team+A+vs+Team+B
    search_query = f"{teams_part if teams else title}".replace(" ", "+")
    espn_link = f"https://www.espncricinfo.com/search?q={search_query}"

    content = f"""---
tags: [cricket, match]
date: {today}
status: {match_data['status']}
teams: {teams}
link: {espn_link}
match_id: {match_data['id']}
---
# {match_data['title']}

**Status**: {match_data['status']}

[View on ESPNcricinfo]({espn_link})
[View on Cricbuzz]({match_data['url']})

## Notes
- 
"""
    
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        return file_path
    except Exception as e:
        print(f"Error creating file: {e}")
        return None
