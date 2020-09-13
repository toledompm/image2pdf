from fpdf import FPDF
from PIL import Image

def pdfGen(pdfFileName, imgList, target):

    cover = Image.open(imgList[0]['path'])
    width, height = cover.size

    pdf = FPDF(unit = "pt", format = [width, height])

    for image in imgList:
        pageWidth, pageHeight = Image.open(image['path']).size
        pdf.add_page('P '+str(pageWidth)+' '+str(pageHeight))
        pdf.image(image['path'], 0, 0)

    pdf.output(target + pdfFileName + ".pdf", "F")
