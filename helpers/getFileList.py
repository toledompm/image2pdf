from os import walk
from os.path import splitext
from os.path import join


def getFileList(path):
    files = []
    for (dirPath, dirNames, fileNames) in walk(path):
        for fileName in fileNames:
            fileExtension = splitext(fileName)[1]
            filePath = join(dirPath, fileName)
            files.append(
                {"path": filePath, "fileName": fileName, "extension": fileExtension}
            )
    return files
