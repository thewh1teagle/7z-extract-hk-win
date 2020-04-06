import win32gui, time
from win32con import PAGE_READWRITE, MEM_COMMIT, MEM_RESERVE, MEM_RELEASE, PROCESS_ALL_ACCESS, WM_GETTEXTLENGTH, WM_GETTEXT
from commctrl import LVS_OWNERDATA, LVM_GETITEMCOUNT, LVM_GETNEXTITEM, LVNI_SELECTED
import os
import struct
import ctypes
import win32api
import datetime
import win32com.client as win32
import win32ui
import psutil
import subprocess
import time
import urllib.parse


def explorer_fileselection():
    clsid = '{9BA05972-F6A8-11CF-A442-00A0C90A8F39}' #Valid for IE as well!
    files = []
    shellwindows = win32.Dispatch(clsid)
    window = win32gui.GetForegroundWindow()
    for window in range(shellwindows.Count):
        selected_files = shellwindows[window].Document.SelectedItems()
        for file in range(selected_files.Count):
            files.append(selected_files.Item(file).Path)
        if len(files) == 1:
            file = files[0]
            return file


def try_to_get_file():
    file = None
    for _ in range(5):
        file = explorer_fileselection()
        print(file)
        if file:
            break
    if file:
        return file
    

def extract_file(path):
    directory = os.path.dirname(os.path.abspath(path))
    os.chdir(directory)
    command = r""" "C:/Program Files/7-Zip/7zG.exe" """  +  "e " +  path 
    print(command)
    os.system(command)


if __name__ == "__main__":
    file = try_to_get_file()
    if file:
        extract_file(file)
