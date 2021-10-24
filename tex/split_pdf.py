from os import lseek
import PyPDF2
import re

filename = YOUR FILE NAME
writer = PyPDF2.PdfFileWriter()
currentlyWritingTo = None
with open(filename, 'rb') as f:
    reader=PyPDF2.PdfFileReader(f)
    for i in range(reader.getNumPages()):
        page = reader.getPage(i)
        text = page.extractText().split('\n')[0:5]
        if text[0].isdigit():
            print(text)
            if currentlyWritingTo:
                print('ok', currentlyWritingTo)
                
                writer.write(open(f"submission/{currentlyWritingTo}.pdf", 'wb'))
                writer = PyPDF2.PdfFileWriter()
                currentlyWritingTo = text[0]
            else:
                print('lawl')
                currentlyWritingTo = text[0]
        writer.addPage(page)
writer.write(open(f"submission/{currentlyWritingTo}.pdf", 'wb'))
writer = PyPDF2.PdfFileWriter()