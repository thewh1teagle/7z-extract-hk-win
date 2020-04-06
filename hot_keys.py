import keyboard 
from os import system

def execute():
    system("python extractor.py")

keyboard.add_hotkey('ctrl + shift + a', execute) 
  
keyboard.wait('esc') 