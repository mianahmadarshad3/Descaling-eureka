# Automated System Maintenance Script

A lightweight Python automation utility that scans a designated folder (like your local Downloads directory), identifies files by their extensions, and cleanly organizes them into categorized subfolders.

## Features
- Safe file path manipulation using Python's modern `pathlib`.
- Skips existing folders to prevent accidental nesting recursive loops.
- Automatically creates destination folders (`Documents`, `Images`, etc.) only when needed.

## How to Run
1. Clone the repository.
2. Open `maintenance.py` and modify the `TARGET_DIR` variable to point to the folder you want to clean.
3. Run the script:
   ```bash
   python maintenance.py