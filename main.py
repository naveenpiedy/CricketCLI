import sys
from InquirerPy import inquirer
from rich.console import Console
from rich.table import Table
from api_client import get_matches
from obsidian_writer import create_match_note

# Config
VAULT_PATH = r"C:\Users\navee\obsidian\Musings\Sports\Cricket"

console = Console()

def main():
    console.print("[bold green]Fetching matches...[/bold green]")
    matches = get_matches()
    
    if not matches:
        console.print("[bold red]No matches found or error fetching data.[/bold red]")
        return

    # Create mapping for autocomplete
    match_map = {f"{m['title']} [{m['status']}]": m for m in matches}

    selected_title = inquirer.fuzzy(
        message="Select a match (type to filter):",
        choices=list(match_map.keys()),
    ).execute()

    if selected_title:
        selected_match = match_map[selected_title]
        console.print(f"[bold blue]Creating note for: {selected_match['title']}[/bold blue]")
        file_path = create_match_note(VAULT_PATH, selected_match)
        
        if file_path:
            console.print(f"[bold green]Successfully created note at:[/bold green] {file_path}")
        else:
            console.print("[bold red]Failed to create note.[/bold red]")

if __name__ == "__main__":
    main()
