import PyPDF2
import sys
import os
from PyPDF2 import PdfFileReader,PdfFileWriter
listOfArgv=sys.argv[1:]

def addWatermark(pdfList):

    watermark=PyPDF2.PdfFileReader(open('wtr.pdf','rb'))#with  as file1:
    output=PyPDF2.PdfFileWriter()
    origFile=PyPDF2.PdfFileReader(open(pdfList[0],'rb'))

    for i in range(origFile.getNumPages()):
        page=origFile.getPage(i)
        page.mergePage(watermark.getPage(0))
        output.addPage(page)

    with open(pdfList[1],'wb') as file:
        output.write(file)


addWatermark(listOfArgv)




