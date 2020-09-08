from shutil import copytree
from os.path import abspath

def moveInputs(path):
    absolutePath = abspath(path)
    copytree(absolutePath,'temp')
