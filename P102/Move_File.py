import os
import shutil

# Define source and destination directories
from_dir = "C:/Users/Faizaan Damji/Downloads/Downloads"
to_dir = "C:/Users/Faizaan Damji/Videos/Document_files"

# Get the list of files from the source directory
list_of_files = os.listdir(from_dir)
print(list_of_files)

# Loop through each file in the list
for file_name in list_of_files:
    # Get the file name and extension
    name, extension = os.path.splitext(file_name)

    # If the extension is blank, skip to the next file
    if extension == '':
        continue

    # Check if the extension is one of the desired document extensions
    if extension in ['.txt', '.doc', '.docx', '.pdf']:
        # Create source and destination paths
        path1 = from_dir + '/' + file_name
        path2 = to_dir
        path3 = to_dir + '/' + file_name

        # Check if the destination directory exists
        if os.path.exists(path2):
            print(f"Moving {file_name}...")
            shutil.move(path1, path3)
        else:
            # Create the destination directory if it does not exist
            os.makedirs(path2)
            print(f"Moving {file_name}...")
            shutil.move(path1, path3)