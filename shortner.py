import os
import pyhk
import subprocess




def func():
    print(subprocess.check_output(['python', 'current_file.py']).decode())

#create pyhk class instance
hot = pyhk.pyhk()
 
#add hotkey
hot.addHotkey(['Ctrl', 'Alt','7'],func)
 
#start looking for hotkey.
hot.start()