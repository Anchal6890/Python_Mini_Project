import json
import shutil

def organize_files_by_extension(folder_path):
    if not os.path.isdir(folder_path):
        print("Invalid folder path.")
        return

    # Loop through all files in the directory
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        #Skip directories
        if os.path.isdir(file_path):
            continue

        # Get the file extension:
        _, extension = os.path.splitext(filename)
        extension = extension[1:].lower()  # remove dot and convert to lower

        if not extension:
            extension = "no_extension"

        # Create a folder for the extension if it doesn't exist
        extension_folder = os.path.join(folder_path,extension)
        if not os.path.exists(extension_folder):
            os.makedirs(extension_folder)

        # Move the file into the corresponding folder
        new_path = os.path.join(extension_folder,filename)
        shutil.move(file_path, new_path)
        print(f"Moved: {filename} --> {extension}")

        
# Main block - this runs when the script is executed
if __name__ == "__main__":
    # You can hardcode a path for testing or ask the user
    
    folder_to_organize = input("C:\\Users\\ADMIN\\Downloads\\New folder")
    organize_folder(folder_path)

        # Call the function AFTER it has been defined

organize_folder(folder_to_organize)
print("\nFile organization complete!")
    
        
