# CodeAlpha Internship Project
# Task 3: File Organizer Automation Script
# Author: <Your Name>
# Date: <Insert Date>

import os
import shutil

def organize_files(source_folder, destination_folder, extensions):
    """
    Move files with specific extensions from the source folder
    to the destination folder automatically.
    """
    # Create destination folder if it doesn't exist
    os.makedirs(destination_folder, exist_ok=True)
    
    files_moved = 0

    # Loop through all files in source folder
    for filename in os.listdir(source_folder):
        # Check if file ends with one of the given extensions
        if filename.lower().endswith(extensions):
            src_path = os.path.join(source_folder, filename)
            dest_path = os.path.join(destination_folder, filename)
            
            shutil.move(src_path, dest_path)
            files_moved += 1
            print(f"✅ Moved: {filename}")

    if files_moved == 0:
        print("⚠️ No matching files found.")
    else:
        print(f"\n🎯 Successfully moved {files_moved} files to '{destination_folder}'.")


if __name__ == "__main__":
    print("📂 File Organizer Automation Script")
    source = input("Enter the source folder path: ").strip()
    destination = input("Enter the destination folder path: ").strip()

    # Example: move all JPG and PNG files
    extensions = (".jpg", ".jpeg", ".png")

    if os.path.exists(source):
        organize_files(source, destination, extensions)
    else:
        print("❌ The source folder does not exist.")
