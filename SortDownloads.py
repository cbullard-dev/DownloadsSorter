#!/usr/bin/env python3

import os
from os import path, getenv, listdir
from sys import argv
import shutil
import log

SUCCESS = 0
ERROR_GENERAL = 1
ERROR_DIRECTORY_NOT_FOUND = 2

DEVELOPER_BUILD = False

IGNORED_FILES = [".DS_Store", ".localized"]

documentTypes = ["pdf", "doc", "docx", "pages", "numbers"]
flatDocumentTypes = ["txt", "csv", "json", "md"]
softwareTypes = ["dmg", "pgk"]
imageTypes = ["cr2", "png", "jpg", "jpeg"]
videoTypes = ["mp4", "mpg", "mpeg"]
diskImageTypes = ["iso"]
subtitleType = ["srt"]
archiveType = ["zip", "tar", "gz"]
windowsTypes = ["exe", "msi"]
ebookTypes = ["mobi","epub"]
calendarTypes = ["ics"]
drawingTypes = ["excalidraw"]

directoriesDict = {
    "documents": documentTypes,
    "text_files": flatDocumentTypes,
    "software": softwareTypes,
    "disk_images": diskImageTypes,
    "images": imageTypes,
    "videos": videoTypes,
    "subtitles": subtitleType,
    "archives": archiveType,
    "windows_junk": windowsTypes,
    "ebooks": ebookTypes,
    "calendar_entries": calendarTypes,
    "digital_drawings": drawingTypes
}

unlistedExtensions = []

homeDirectory = getenv("HOME")

downloadPath: str = f"{homeDirectory}/Downloads"

if DEVELOPER_BUILD:
    downloadPath = path.join(downloadPath, "TESTING")


def main(args: list[str]) -> int:
    dry_run = False
    for arg in args:
        if(arg=="-d" or arg=="--dry-run"):
            log.info("Starting dry-run!")
            dry_run = True
    # Check if the directories exist, if not, create them
    for dir in directoriesDict:
        if not directoryExist(dir):
            createDirectory(dir)
    # For each file gather the data on the file and if it should be moved
    for file in listdir(downloadPath):
        if file in IGNORED_FILES: continue
        result = checkExtension(file)
        if result == "Is directory": continue
        if result in directoriesDict:
            log.debug(f"The type result is {result}")
            file = path.join(downloadPath, file)
            dest = path.join(downloadPath, result)
            fileNewPath = ''
            if not dry_run:
                fileNewPath = copyFiles(file, dest)
        else:
            log.warn(f"Was unable to copy {file} because {result}")
            continue

        # Check each file has successfully been created
        if dry_run: continue
        if validateNewFile(fileNewPath):
            os.remove(file)
    duplicateFreeUnlistedExtensions = set(unlistedExtensions)
    if len(duplicateFreeUnlistedExtensions) > 1:
        log.info(f"The following were unsorted file extensions:\n{duplicateFreeUnlistedExtensions}")
    if dry_run:
        log.info("Dry-run completed!")
    else:
        log.info("Execution completed!")
    return 1


def checkDestinationExists(destinationPath: str) -> bool:
    return path.exists(destinationPath)


def createDirectory(directoryName: str) -> None:
    newPath = path.join(downloadPath, directoryName)
    os.mkdir(newPath)
    log.info(f"Created {directoryName} at path {newPath}")


def directoryExist(directory: str) -> bool:
    dirPath = path.join(downloadPath, directory)
    dirExists = checkDestinationExists(dirPath)
    log.info(f"Does the directory '{directory}' exist: {dirExists}")
    return dirExists


def checkExtension(file: str) -> str:
    fileBreakdown = file.split(".")
    name = ""
    extension = ""
    if path.isdir(path.join(downloadPath, file)):
        return "Is directory"
    if len(fileBreakdown) <= 1:
        return "No file extension"
    else:
        name = path.splitext(file)[0]
        log.debug(f"The file name is {name}")
        extension = fileBreakdown[-1].lower()
    for category, ext in directoriesDict.items():
        if extension in ext:
            return category
    unlistedExtensions.append(extension)
    return f"File {name} with extension {extension} has no defined category!"


def copyFiles(file: str, destination: str) -> str:
    try:
        result = shutil.copy2(file, destination)
    except shutil.SameFileError:
        return f"ERROR: File same as destination"
    return result


def validateNewFile(newPath: str) -> bool:
    return path.exists(newPath)


if __name__ == "__main__":
    import sys

    sys.exit(main(argv))
