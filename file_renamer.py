import os

def replace_special_characters(filename):
    # Define umlaut replacement mapping
    umlaut_replacements = {
        'ä': 'ae',
        'ö': 'oe',
        'ü': 'ue',
    }
    
    # Replace umlauts
    for umlaut, replacement in umlaut_replacements.items():
        filename = filename.replace(umlaut, replacement)

    # Replace spaces with underscores
    filename = filename.replace(' ', '_')
    
    return filename

def rename_files_in_folder(folder_path):
    for root, _, files in os.walk(folder_path):
        for filename in files:
            old_filepath = os.path.join(root, filename)
            new_filename = replace_special_characters(filename)
            new_filepath = os.path.join(root, new_filename)
            
            if old_filepath != new_filepath:
                os.rename(old_filepath, new_filepath)
                print(f'Renamed: {filename} -> {new_filename}')

if __name__ == '__main__':
    folder_path = 'GTP4'  # Replace with your folder path
    rename_files_in_folder(folder_path)
