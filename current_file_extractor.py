import win32gui
import os
import win32com.client as win32



def explorer_fileselection():
    clsid = '{9BA05972-F6A8-11CF-A442-00A0C90A8F39}' #Valid for IE as well!
    files = []
    shellwindows = win32.Dispatch(clsid)
    window = win32gui.GetForegroundWindow()
    for window in range(shellwindows.Count):
        selected_files = shellwindows[window].Document.SelectedItems()
        for file in range(selected_files.Count):
            files.append(selected_files.Item(file).Path)
    return files


def try_to_get_files():
    for _ in range(3):
        files = explorer_fileselection()
        if len(files):
            return files


def extract_file(path):
    directory = os.path.dirname(os.path.abspath(path))
    os.chdir(directory)
    command = '"C:/Program Files/7-Zip/7zG.exe" e {}'.format(path)
    print(command)
    os.system(command)


if __name__ == "__main__":
    if files := try_to_get_files():
        for file in files:
            extract_file(file) 
        
