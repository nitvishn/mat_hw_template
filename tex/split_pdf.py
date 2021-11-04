from os import lseek
import PyPDF2
import re

filename = 'mat157_hw6.pdf'
writer = PyPDF2.PdfFileWriter()
currentlyWritingTo = None
with open(filename, 'rb') as f:
    reader=PyPDF2.PdfFileReader(f)
    for i in range(reader.getNumPages()):
        page = reader.getPage(i)
        text = page.extractText().split('\n')[0:10]
        # print(text)
        if re.search(r'^[0-9]+[a-zA-Z0-9:),\']*$', text[0]):
            questionFound = int(re.search(r'\d+', text[0]).group())
            print(f"Found question {questionFound} on page {i+1}. We are currently writing to {currentlyWritingTo}.")
            if currentlyWritingTo:
                if questionFound == currentlyWritingTo + 1:
                    print(f"Wrapping up question {currentlyWritingTo}.")
                    writer.write(open(f"submission/{currentlyWritingTo}.pdf", 'wb'))
                    writer = PyPDF2.PdfFileWriter()
                    currentlyWritingTo = questionFound
            else:
                currentlyWritingTo = questionFound
        writer.addPage(page)
print(f"Finishing up by writing to {currentlyWritingTo}")
writer.write(open(f"submission/{currentlyWritingTo}.pdf", 'wb'))
writer = PyPDF2.PdfFileWriter()