from os import lseek
import PyPDF2
import re

filename = 'mat157_hw5.pdf'
writer = PyPDF2.PdfFileWriter()
currentlyWritingTo = None
with open(filename, 'rb') as f:
    reader=PyPDF2.PdfFileReader(f)
    for i in range(reader.getNumPages()):
        page = reader.getPage(i)
        text = page.extractText().split('\n')[0:5]
        if re.search(r'^[0-9]+[a-zA-Z0-9:),\']*$', text[0]) :
            print(text[0])
            if currentlyWritingTo:
                print('ok', currentlyWritingTo)
                
                writer.write(open(f"submission/{currentlyWritingTo}.pdf", 'wb'))
                writer = PyPDF2.PdfFileWriter()
                currentlyWritingTo = text[0][0]
            else:
                print('lawl')
                currentlyWritingTo = text[0][0]
        writer.addPage(page)
writer.write(open(f"submission/{currentlyWritingTo}.pdf", 'wb'))
writer = PyPDF2.PdfFileWriter()