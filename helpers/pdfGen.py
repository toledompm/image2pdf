from fpdf import FPDF
from PIL import Image

def pdfGen(pdfFileName, imgList, target):

    cover = Image.open(imgList[0]['path'])
    width, height = cover.size

    pdf = FPDF(unit = "pt", format = [width, height])

    for page in imgList:
        pdf.add_page()
        pdf.image(page['path'], 0, 0)

    pdf.output(target + pdfFileName + ".pdf", "F")
