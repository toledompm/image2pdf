# image2pdf

Packages images from a directory into a pdf. Also include helper modules to unzip images, default ordering for pdf is alphabetical, but can be tweaked by creating a file in the root of the directory named **SortSettings.py**

Setup
-----
``pip install fpdf``

``pip install Pillow``

Usage
-----

execute

``python main.py``

It will ask you for a path to your image directory (if left blank the script will look for a folder named **inputs/** in the root of the directory). After that the contents of the folder you specified will be copied to a temporary place, all zips will be unziped and finaly, a pdf will be generated from the images the script found (ps: only png and jpg rn)

### SortSettings
