import keyboard 
from os import system

def execute():
    system("python current_file_extractor.py")

keyboard.add_hotkey('ctrl + shift + a', execute) 
keyboard.wait() 