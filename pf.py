#!/usr/bin/env python

from PyPDF2 import PdfFileWriter, PdfFileReader 
output = PdfFileWriter() # open output
i1=open('myresume.pdf', 'rb')
input = PdfFileReader(i1) # open input
output.addPage(input.getPage(0)) # insert page
output.addBookmark('Hello, World', 0, parent=None) # add bookmark