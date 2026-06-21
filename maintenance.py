import os
from pathlib import Path

# Define the folder you want to clean up (Defaults to the current directory)
TARGET_DIR = Path(".")

# Define your file categories and their respective extensions
TRACKED_EXTENSIONS = {
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Scripts_and_Code": [".py", ".js", ".html", ".css", ".json", ".sh"]
}

def organize_folder():
    print(f"Scanning directory: {TARGET_DIR.resolve()}\n")
    
    # Track files moved to show a summary at the end
    moved_count = 0

    # Loop through every item in the target directory
    for item in TARGET_DIR.iterdir():
        # Skip directories, the script itself, and git folders
        if item.is_dir() or item.name in ["maintenance.py", "upload.py", ".gitignore"]:
            continue
            
        file_extension = item.suffix.lower()
        
        # Check which category the file matches
        for folder_name, extensions in TRACKED_EXTENSIONS.items():
            if file_extension in extensions:
                # Create the destination folder if it doesn't exist yet
                destination_folder = TARGET_DIR / folder_name
                destination_folder.mkdir(exist_ok=True)
                
                # Move the file securely
                new_path = destination_folder / item.name
                item.rename(new_path)
                
                print(f"Moved: {item.name} -> {folder_name}/")
                moved_count += 1
                break # Stop checking other categories once matched

    print(f"\n✨ Cleanup finished! Total files organized: {moved_count}")

if __name__ == "__main__":
    organize_folder()