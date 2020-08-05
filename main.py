import os
import sys
import shutil

# Gets the folder path to organize
folderPath = sys.argv[1]

# Goes to the specified folder
os.chdir(folderPath)

# Tuple of file formats
imageFormats = (".png", ".jpg", ".jpeg", ".gif")
videoFormats = (".mp4", ".mov", ".avi")
audioFormats = (".mp3", ".wav", ".aiff")
docsFormats = (".pdf", ".docx", ".pptx", ".txt")

# Scans all the files types and move them to the correct folder
for file in os.listdir(folderPath):
    # If the file is a folder the program will ignore it
    if os.path.isdir(folderPath+'/'+file):
        continue
    if file.endswith(imageFormats):
        try:
            os.mkdir('./DownloadedImages')
        except:
            print("Folder already exists")
        shutil.move(file, './DownloadedImages')
    elif file.endswith(videoFormats):
        try:
            os.mkdir('./DownloadedImages')
        except:
            print("Folder already exists")
        shutil.move(file, './DownloadedVideos')
    elif file.endswith(audioFormats):
        try:
            os.mkdir('./DownloadedAudios')
        except:
            print("Folder already exists")
        shutil.move(file, './DownloadedAudios')
    elif file.endswith(docsFormats):
        try:
            os.mkdir('./DownloadedDocs')
        except:
            print("Folder already exists")
        shutil.move(file, './DownloadedDocs')
    else:
        try:
            os.mkdir('./DownloadedMisc')
        except:
            print("Folder already exists")
        shutil.move(file, './DownloadedMisc')
        
print("CLEANUP COMPLETED !!!")