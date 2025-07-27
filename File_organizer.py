import os
import shutil

def create_folder_if_not_exists(folder_path):
    """Creates a folder if it doesn't already exists."""
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

def organize_files(source_dir):
    """Organizes files in the specified directory."""

    # Define common extensions and their target folder names
    extensions_map = {
        'images':['.jpg','.jpeg','.png','.gif','.bmp','.tiff','.webp'],
        'documents':['.pdf','.doc','.docx','.txt','.xlsx','.xls','.ppt','.pptx'],
        'archives':['.zip','.rar','.7z','.tar','.gz'],
        'audio':['.mp3','.wav','.aac','.flac'],
        'video':['.mp4','.avi','.mkv','.mov'],
        'executables':['.exe','.msi','.dmg','.deb','.rpm'],
        'code':['.py','.js','.html','.css','.c','.cpp','.java'],
        'other':[] # Default category for unmapped files
        }

    # Create reverse lookup dictionary for extensions
    file_categories = {}
    for category,exts in extensions_map.items():
        for ext in exts:
            file_categories[ext.lower()] = category

            try:
                for filename in os.listdir(source_dir):
                    source_path = os.path.join(source_dir,filename)

    # Skip directories
    if os.path.isdir(source_path):
        continue

    # Get file extension
    _,extension = os.path.splitex(filename)
    extension = extension.lower()

for ext in exts:
            file_categories[ext.lower()] = category

    try:
        for filename in os.listdir(source_dir):
            source_path = os.path.join(source_dir,filename)
        

    # Skip directories
    if os.path.isdir(source_path):
        continue

    # Get file extension
    _, extension = os.path.splitext(filename)
    extension = extension.lower()
    
    

    # Get category,default to 'others'
    target_category = file_categories.get(extension,'others')

    # Set folder name same as category,capitalize first letter
    target_dir_name = target_category.capitalized()if target_category!='others'else'Others'
    destination_folder = os.path.join(source_dir,target_dir_name)

    # Create folder if it does not exist
    create_folder_if_not_exists(destination_folder)
    
    destination_path = os.path.join(destination_folder,filename)

    # Avoid overwriting files
    if os.path.exists(destination_path):
        print(f"Skipping'{filename}'(already exists in '{target_dir_name}')")
        continue

    shutil.move(source_path,destination_path)
    print(f"Moved'{filename}'to'{target_dir_name}")

except FileNotFoundError:
    print(f"Error:Source directory not found at'{source_dir}")
except PermissionError:
    print(f"Error:Permission denied.Check your access rights.")
except Exception as e:
    print(f"An unexpected error occurred:{e}")
    
        
        
    
    
    
