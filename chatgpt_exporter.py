import zipfile

# Define the path to the zip file and the extraction directory
zip_file_path = "/workspaces/quantified_chatgpt/data/obsidian_import (2).zip"
extract_to_path = "data/obsidian_extracted"

# Unzip the uploaded file
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(extract_to_path)
