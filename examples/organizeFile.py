import os
from pathlib import Path


absolutePath = "/Users/handrywahyudi/Documents/"
picturesPath = "/Users/handrywahyudi/Pictures/"


SUBDIRECTORIES = {
    absolutePath + "Docs": ['.doc', '.txt', '.docx', '.zip'],
    absolutePath + "Books": ['.pdf', '.epub'],
    absolutePath + "Installer": ['.dmg','.iso', '.app', '.exe'],
    picturesPath: ['.jpg', '.jpeg'],
    absolutePath + "Movies": ['.mp4', '.mkv', '.mp3', '.srt']
}


def pickDirectory(value):
    for category, extensions in SUBDIRECTORIES.items():
        for extension in extensions:
            if extension == value:
                return category
    return absolutePath + 'Misc'


def organizeDirectory():
    for item in os.scandir():
        if item.is_dir():
            continue

        filePath = Path(item)
        fileType = filePath.suffix.lower()
        directory = pickDirectory(fileType)
        directoryPath = Path(directory)

        if fileType == '.py':
            continue

        filePath.rename(directoryPath.joinpath(filePath))


organizeDirectory()

