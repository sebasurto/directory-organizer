import os
import shutil

directory = os.getcwd().encode()
files = os.listdir(directory)
#remenber use setGloblas 
def organize_file_by_extension (directory_new):
    setGlobals(directory_new)
    global directory,files 
    files_by_extension = create_dict_with_files_and_extension ()
    for extension, file_list in files_by_extension.items():
        folder_extension = os.path.join(directory, extension)

        if not os.path.exists(folder_extension):
                os.mkdir(folder_extension)

        for file in file_list:
            origin = os.path.join(directory, file)
            destination = os.path.join(folder_extension, file)
            shutil.move(origin, destination)

def create_dict_with_files_and_extension ():
    global files
    files_by_extension = {}

    for file in files:
        if os.path.isfile(os.path.join(directory, file)):
            extension = os.path.splitext(file)[1]

            if extension not in files_by_extension:
                files_by_extension[extension] = []
        
            files_by_extension[extension].append (file)
    return files_by_extension

def setGlobals(new_directory):
    global directory, files
    directory = new_directory
    files = os.listdir(directory)