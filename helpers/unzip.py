from zipfile import ZipFile
from os import remove
from os.path import join

def unzip(path,targetDir):
    with ZipFile(path) as file:
        for filename in file.namelist():
            file.extract(filename,join(targetDir,path))
    remove(path)