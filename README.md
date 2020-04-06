# 7z-extract-hk-win
Enable hot key for fast extraction of files in windows with 7zip program

![Untitled](https://user-images.githubusercontent.com/61390950/78570664-f0616e80-782d-11ea-87b8-286fb060982d.png)

requirements:

  python3 https://www.python.org
  
  7zip https://www.7-zip.org/download.html
  
  keyboard module:
    pip install keyboard
    pip install pywin32

current_file_extractor.py
  
  what the script do is to find the current selected file in files explorer window in windows 
  and then he try to extract the file with 7zip. 
  instead of : 
  
  right click > extract files > extract 
  
 hot_keys.py
  
  the script just bind for your hot keys and when you hit them ( when you select the file )
  
  the script execute current_file_extractor.py
 
