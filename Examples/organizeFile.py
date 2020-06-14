#!/usr/local/bin/python3
import os
from pathlib import Path
import argparse
import sys
import shutil


absolutePath = "/Users/handrywahyudi/Documents/"
picturesPath = "/Users/handrywahyudi/Pictures/"


SUBDIRECTORIES = {
    absolutePath + "Docs": ['doc', 'txt', 'docx', 'zip'],
    absolutePath + "Books": ['pdf', 'epub'],
    absolutePath + "Installer": ['dmg','iso', 'app', 'exe'],
    picturesPath: ['jpg', 'jpeg'],
    absolutePath + "Movies": ['mp4', 'mkv', 'mp3', 'srt']
}


def pickDirectory(value):
    for category, extensions in SUBDIRECTORIES.items():
        for extension in extensions:
            if extension == value:
                return category
    return absolutePath + 'Misc'


def moveFile(fileType):
    fileTypeReg = '.' + fileType
    for file in os.listdir('./'):
            if file.endswith(fileTypeReg):
                directory = pickDirectory(fileType)
                try:
                    new_path = shutil.move(file, directory)
                    print(new_path)
                except Exception as e:
                    print(e)


def organizeDirectory(fileType):
    if fileType == 'pdf':
        moveFile(fileType)
    elif fileType == 'doc':
        moveFile(fileType)
    elif fileType == 'txt':
        moveFile(fileType)
    elif fileType == 'docx':
        moveFile(fileType)
    elif fileType == 'zip':
        moveFile(fileType)
    elif fileType == 'epub':
        moveFile(fileType)
    elif fileType == 'dmg':
        moveFile(fileType)
    elif fileType == 'iso':
        moveFile(fileType)
    elif fileType == 'app':
        moveFile(fileType)
    elif fileType == 'exe':
        moveFile(fileType)
    elif fileType == 'jpg':
        moveFile(fileType)
    elif fileType == 'jpeg':
        moveFile(fileType)
    elif fileType == 'mp4':
        moveFile(fileType)
    elif fileType == 'mkv':
        moveFile(fileType)
    elif fileType == 'mp3':
        moveFile(fileType)
    elif fileType == 'srt':
        moveFile(fileType)


if __name__ == "__main__":
    my_parser = argparse.ArgumentParser(prog='organizeFile', usage='%(prog)s [options] FILETYPE', description='Move my files on downloads to their correct folder.')
    my_parser.add_argument('-t', '--type', type=str, help='Choose of your file type.')
    args = my_parser.parse_args()

    if args.type == 'pdf':
        organizeDirectory('pdf')
    elif args.type == 'doc':
        organizeDirectory('doc')
    elif args.type == 'docx':
        organizeDirectory('docx')
    elif args.type == 'zip':
        organizeDirectory('zip')
    elif args.type == 'epub':
        organizeDirectory('epub')
    elif args.type == 'dmg':
        organizeDirectory('dmg')
    elif args.type == 'iso':
        organizeDirectory('iso')
    elif args.type == 'app':
        organizeDirectory('app')
    elif args.type == 'exe':
        organizeDirectory('exe')
    elif args.type == 'jpg':
        organizeDirectory('jpg')
    elif args.type == 'jpeg':
        organizeDirectory('jpeg')
    elif args.type == 'mp4':
        organizeDirectory('mp4')
    elif args.type == 'mkv':
        organizeDirectory('mkv')
    elif args.type == 'mp3':
        organizeDirectory('mp3')
    elif args.type == 'srt':
        organizeDirectory('srt')
    elif args.type == 'py':
        organizeDirectory(args.type)
