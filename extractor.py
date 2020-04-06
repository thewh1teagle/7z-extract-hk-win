import os
import current_file

def try_to_get_file():
    file = None
    for _ in range(5):
        file = current_file.explorer_fileselection()
        print(file)
        if file:
            break
    if file:
        return file
    

def extract_file(path):
    os.system(r""" "C:/Program Files/7-Zip/7zG.exe" """ + "a " + path )


if __name__ == "__main__":
    file = try_to_get_file()
    if file:
        extract_file(file)
