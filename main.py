import zipfile
import os
import gdown

# Path to the desired download directory
download_directory = 'download'
file_path = os.path.join(download_directory)
# Change the working directory
os.chdir(file_path)


url = "https://drive.google.com/file/d/194iOp51kusAsuK_LVIO4fca1ep6CDWrZ/view?usp=drive_link"
# gdown.download(url =url,fuzzy=True)


# Path to the folder
folder_path = 'download'

# List of files to check
files_to_check = ['a.zip']

# Loop through each file and check if it exists in the folder
for file_name in files_to_check:
    # Full path to the file
    file_path = os.path.join( file_name)
    
    # Check if the file exists
    if os.path.isfile(file_path):
       
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            zip_ref.extractall(os.path.join(""))
    else:
        print(f"'{file_name}' is not present in the '{folder_path}' folder.")
print("done")