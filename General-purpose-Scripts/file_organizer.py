from pathlib import Path
import shutil

# sorts cluttered files into folders based on their file extensions
# Can be used to clean up a messy directory structure

# setting the folder you want to organize
# replace this with the path to your folder on your machine
folder_to_organize = Path("path/to/your/folder")

#match file extentions to their respective folders
file_categories = {
    ".pdf": "PDFs",
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".xlsx": "Spreadsheets",
    ".csv":"Spreadsheets",
    ".txt": "Text Files",
    ".py": "Python Scripts",
    ".docx": "Word Documents",
    ".doc": "Word Documents",
    ".mp3": "Audio Files",
    ".wav": "Audio Files",
    ".mp4": "Videos",
    ".mov": "Videos"
}

# check whether the folder exists
if not folder_to_organize.is_dir():
    print(f"Error: The folder '{folder_to_organize}' does not exist.")
else:
    # Get the items inside the folder.
    for file_path in folder_to_organize.iterdir():

        # Skip anything that isn't a file.
        if not file_path.is_file():
            continue

        # Get the file extension in lowercase.
        extension = file_path.suffix.lower()

        # Find the destination folder for this extension.
        category = file_categories.get(extension)

        # Skip files with unsupported extensions.
        if category is None:
            print(f"Skipped: {file_path.name} (unsupported file type)")
            continue

        # Create the destination folder path.
        destination_folder = folder_to_organize / category

        # Create the folder if it doesn't already exist.
        destination_folder.mkdir(exist_ok=True)

        # Create the complete destination file path.
        destination_file = destination_folder / file_path.name

        # Avoid overwriting a file with the same name.
        if destination_file.exists():
            print(f"Skipped: {file_path.name} (file already exists)")
            continue

        # Move the file to its destination.
        try:
            shutil.move(str(file_path), str(destination_file))
            print(f"Organized: {file_path.name} -> {category}")

        except OSError as error:
            print(f"Error moving {file_path.name}: {error}")

    print("\nFile organization complete!")