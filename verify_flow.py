import os
import shutil
from api_client import get_matches
from obsidian_writer import create_match_note

TEST_VAULT = r"C:\Users\navee\AntiGravity\CricketCLI\test_vault"

def verify():
    print("Fetching matches...")
    matches = get_matches()
    if not matches:
        print("No matches found!")
        return

    print(f"Found {len(matches)} matches.")
    first_match = matches[0]
    print(f"Selecting first match: {first_match['title']}")

    print(f"Creating note in {TEST_VAULT}...")
    file_path = create_match_note(TEST_VAULT, first_match)
    
    if file_path and os.path.exists(file_path):
        print(f"SUCCESS: File created at {file_path}")
        with open(file_path, "r", encoding="utf-8") as f:
            print("--- File Content ---")
            print(f.read())
            print("--------------------")
    else:
        print("FAILURE: File not created.")

    # Cleanup
    # shutil.rmtree(TEST_VAULT)

if __name__ == "__main__":
    verify()
