from shutil import copytree
from os import chdir
from os.path import abspath

def moveInputs(path):
    absolutePath = abspath(path)
    copytree(absolutePath,'temp')
