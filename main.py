import os
import sys
import shutil

# Gets the folder path to organize
folderPath = sys.argv[1]

# Goes to the specified folder
os.chdir(folderPath)

# Creates the 4 organizational folders
os.mkdir('./DownloadedImages')
os.mkdir('./DownloadedVideos')
os.mkdir('./DownloadedAudios')
os.mkdir('./DownloadedMisc')

# # Scans all the files types and move them to the correct folder
for file in os.listdir(folderPath):
    # If the file is a folder the program will ignore it
    if os.path.isdir(folderPath+'/'+file):
        continue
    if file.endswith(".png") or file.endswith(".jpg") or file.endswith(".tiff") or file.endswith(".svg"):
        shutil.move(file, './DownloadedImages')
    elif file.endswith(".mp4") or file.endswith(".mov") or file.endswith(".avi") or file.endswith(".wmv") or file.endswith(".flv"):
        shutil.move(file, './DownloadedVideos')
    elif file.endswith(".mp3") or file.endswith(".wav") or file.endswith(".aiff"):
        shutil.move(file, './DownloadedAudios')
    else:
        shutil.move(file, './DownloadedMisc')
        
print("CLEANUP COMPLETED !!!")