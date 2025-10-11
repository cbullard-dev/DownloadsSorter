import os
from os import path, getenv, listdir

SUCCESS = 0
ERROR_GENERAL = 1
ERROR_DIRECTORY_NOT_FOUND = 2

documentTypes = ["pdf", "doc", "docx", "pages", "numbers"]
softwareTypes = ["dmg", "pgk"]
imageTypes = ["CR2", "png", "jpg", "jpeg"]
diskImageTypes = ["iso"]
subtitleType = ["srt"]
archiveType = ["zip", "tar", "gz"]

directoriesDict = {
    "Documents": documentTypes,
    "Software": softwareTypes,
    "Disk_Images": diskImageTypes,
    "Images": imageTypes,
    "Subtitles": subtitleType,
    "Archives": archiveType,
}

homeDirectory = getenv("HOME")

downloadPath = f"{homeDirectory}/Downloads/TESTING"


def main():
    for dir in directoriesDict:
        if not directoryExist(dir):
            createDirectory(dir)
    print(len(listdir(downloadPath)))
    for file in listdir(downloadPath):
        print(checkExtension(file))
    return 1


def checkDestinationExists(destinationPath: str):
    return path.exists(destinationPath)


def createDirectory(directoryName: str):
    newPath = path.join(downloadPath, directoryName)
    os.mkdir(newPath)
    print(f"Created {directoryName} at path {newPath}")


def directoryExist(directory: dict) -> bool:
    dirPath = path.join(downloadPath, directory)
    dirExists = checkDestinationExists(dirPath)
    print(f"Does the directory '{directory}' exist: {dirExists}")
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
        name = fileBreakdown[0]
        extension = fileBreakdown[-1]
    for category, ext in directoriesDict.items():
        if extension in ext:
            return category
    return f"File {name} with extension {extension} has no defined category!"


if __name__ == "__main__":
    import sys

    sys.exit(main())
