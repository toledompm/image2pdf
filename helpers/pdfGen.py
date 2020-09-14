from fpdf import FPDF
from PIL import Image

def pdfGen(pdfFileName, imgList, target):

    cover = Image.open(imgList[0]['path'])
    width, height = cover.size

    pdf = FPDF(unit = "pt", format = [width, height])

    for image in imgList:

        img = Image.open(image['path'])
        wpercent = (width/float(img.size[0]))
        hsize = int((float(img.size[1])*float(wpercent)))
        img = img.resize((width,hsize), Image.ANTIALIAS)
        img.save(image['path'])
        

        pdf.add_page()
        pdf.image(image['path'], 0, 0)

    pdf.output(target + pdfFileName + ".pdf", "F")
