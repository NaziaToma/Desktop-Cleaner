import os
import fnmatch
import shutil
from pathlib import Path

def get_desktop_path():
    # Check for OneDrive Desktop
    onedrive_path = Path.home() / 'OneDrive' / 'Desktop'
    if onedrive_path.exists():
        return onedrive_path
    return Path.home() / 'Desktop'

file_path = get_desktop_path()

#make a new Folder called Desktop Organizer and send all the new folders to that folder

#file_path = r"C:/Users/ntaba/OneDrive/Desktop"
files_in_dir= os.listdir(file_path)
#change this to work on any desktop


#creates new directory if folder does not exist
def create_new_directory(file, file_type):
    new_folder_name= file_type.replace('*.', '')
    new_folder_path= file_path/new_folder_name
    
    if not os.path.exists(new_folder_path):
        os.makedirs(new_folder_path)
        shutil.move(file_path/file, new_folder_path)
    else:
        shutil.move(file_path/file, new_folder_path)
    

def file_cleaning_method(file_type):
    for file in files_in_dir:
        if fnmatch.fnmatch(file, file_type):
            create_new_directory(file, file_type)
#print (files_in_dir)

file_types_to_clean= ['*.py', '*.cpp','*.pdf','*.zip','*.c','*.jpg','*.png','*.exe','*.obj','*.plantuml','*.wsd', '*docx', '*doc']
        

for files in file_types_to_clean:
    file_cleaning_method(files)
    



#search in the directory
#if found any file with name .py on desktop ->  shift it to one folder



