from os.path import abspath
from shutil import rmtree

from helpers.getFileList import getFileList
from helpers.unzip import unzip
from helpers.dictListFilter import dictListFilter
from helpers.moveInputs import moveInputs
from helpers.pdfGen import pdfGen

inputsPath = input('Enter the path to your image directory: ')
inputsPath = inputsPath if inputsPath != '' else 'inputs'

moveInputs(inputsPath)
zipFileList = dictListFilter(getFileList('temp'),'extension','.zip')

for zip in zipFileList:
    unzip(zip['path'],'temp')

imageFileList = dictListFilter(getFileList('temp'),'extension',['.jpg','.jpeg','.png'])

pdfGen("output",imageFileList,'')

rmtree(abspath('temp'))
