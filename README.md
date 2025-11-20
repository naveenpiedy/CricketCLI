# Cricket Match Obsidian CLI

A Python command-line tool that scrapes live cricket match data from Cricbuzz and generates formatted Markdown notes for your Obsidian vault.

## Features

- **Live Data Fetching**: Scrapes real-time match data from Cricbuzz.
- **Interactive Selection**: Uses a fuzzy search interface to select matches.
- **Obsidian Integration**: Automatically creates Markdown files with match metadata (ID, Status, URL) in your specified Obsidian vault.
- **Rich UI**: Uses `rich` for formatted console output.

## Prerequisites

- Python 3.7+
- An Obsidian vault

## Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd CricketCLI
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Configuration

1.  Open `main.py`.
2.  Update the `VAULT_PATH` variable to point to your desired Obsidian folder:
    ```python
    VAULT_PATH = r"C:\Path\To\Your\Obsidian\Vault\Sports\Cricket"
    ```

## Usage

Run the main script:

```bash
python main.py
```

1.  The tool will fetch currently live and recent matches.
2.  Use the arrow keys or type to filter and select a match from the list.
3.  Press **Enter** to confirm.
4.  A new note will be created in your configured Obsidian folder.

## Project Structure

- `main.py`: Entry point of the application. Handles user interaction and file creation.
- `api_client.py`: Handles scraping and parsing data from Cricbuzz.
- `obsidian_writer.py`: Logic for formatting and writing the Markdown file.
- `requirements.txt`: List of Python dependencies.

## Dependencies

- `requests`: For making HTTP requests.
- `beautifulsoup4`: For parsing HTML.
- `lxml`: HTML parser.
- `rich`: For terminal formatting.
- `InquirerPy`: For interactive command-line prompts.

Link to my [blog post](https://www.npiedy.com/cricket-scraper-obsidian-antigravity/)! If you want to read on how I built this tool.
