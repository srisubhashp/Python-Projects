import PyPDF2
import sys

listOfArg=sys.argv[1:]

def pdfMerger(pdf_list):
    merger=PyPDF2.PdfFileMerger()
    for pdfFile in pdf_list:
        merger.append(pdfFile)
    merger.write('super.pdf')

pdfMerger(listOfArg)