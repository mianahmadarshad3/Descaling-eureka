import os
import shutil
from datetime import datetime
from pathlib import Path

# Define the directory you want to clean up
TARGET_DIR = Path.home() / "Downloads"  # Adjust this path as needed

# Define your file categories mappings
FILE_CATEGORIES = {
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".svg"],
    "Archives": [".zip", ".tar", ".gz", ".rar"],
    "Scripts_and_Code": [".py", ".js", ".html", ".css", ".json"],
}


def organize_folder(target_path):
    target_path = Path(target_path)

    if not target_path.exists():
        print(f"Error: The directory {target_path} does not exist.")
        return

    print(f"[{datetime.now()}] Starting maintenance on: {target_path}")

    # Iterate through all items in the target directory
    for item in target_path.iterdir():
        # Skip directories to avoid messing up existing folders
        if item.is_dir():
            continue

        file_extension = item.suffix.lower()
        moved = False

        # Find the matching category for the file extension
        for category, extensions in FILE_CATEGORIES.items():
            if file_extension in extensions:
                dest_dir = target_path / category
                dest_dir.mkdir(exist_ok=True)  # Create the category folder if it doesn't exist

                print(f"Moving: {item.name} -> {category}/")
                shutil.move(str(item), str(dest_dir / item.name))
                moved = True
                break

        # Optional: Move unknown file types to an "Others" folder
        if not moved and file_extension != "":
            other_dir = target_path / "Others"
            other_dir.mkdir(exist_ok=True)
            shutil.move(str(item), str(other_dir / item.name))

    print(f"[{datetime.now()}] Maintenance complete workflow cleanly executed.")


if __name__ == "__main__":
    organize_folder(TARGET_DIR)