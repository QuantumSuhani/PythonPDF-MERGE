'''...................................................program to merge multiple pdf fies....................................'''
import PyPDF2                     #PyPDF2 it is a library used to merge,split,rotate and manipulate pdf files
pdfiles=["PYTHON.pdf","S1.pdf"]
merger=PyPDF2.PdfMerger()
for filename in pdfiles:
    pdfFile=open(filename,'rb')

    pdfReader = PyPDF2.PdfReader(pdfFile)
    merger.append(pdfReader)
    pdfFile.close()
    merger.write('merged.pdf')
