
from pathlib import Path
import shutil

# Specify the folder you want to back up.
source_folder = Path("my_documents")

# Specify where the backup should be stored.
backup_folder = Path("my_documents_backup")

# Check whether the source folder exists.
if not source_folder.is_dir():
    print("Error: The source folder does not exist.")

# Prevent the backup folder from being inside the source folder.
elif backup_folder.resolve().is_relative_to(source_folder.resolve()):
    print("Error: The backup folder cannot be inside the source folder.")

else:
    # Create the backup folder if it doesn't exist.
    backup_folder.mkdir(parents=True, exist_ok=True)

    # Keep track of how many files are copied.
    files_copied = 0

    # Examine each item in the source folder.
    for item in source_folder.iterdir():

        # Only back up files, not subfolders.
        if not item.is_file():
            continue

        # Create the destination path.
        destination = backup_folder / item.name

        try:
            # Copy the file only if it is new or has changed.
            if (
                not destination.exists()
                or item.stat().st_size != destination.stat().st_size
                or item.stat().st_mtime > destination.stat().st_mtime
            ):
                shutil.copy2(item, destination)

                print(f"Backed up: {item.name}")
                files_copied += 1

            else:
                print(f"Skipped: {item.name} (already up to date)")

        except OSError as error:
            print(f"Error backing up {item.name}: {error}")

    # Display the final result.
    print(f"\nBackup complete! Files copied: {files_copied}")
