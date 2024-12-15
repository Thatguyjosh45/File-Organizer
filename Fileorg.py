import os
import shutil

def organize_files(directory):
    if not os.path.exists(directory):
        print("Directory not found.")
        return

    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)

        if os.path.isfile(file_path):
            file_type = file.split('.')[-1]
            folder = os.path.join(directory, file_type)

            os.makedirs(folder, exist_ok=True)
            shutil.move(file_path, folder)
            print(f"Moved: {file} -> {folder}")

directory = input("Enter the path of the directory to organize: ")
organize_files(directory)
