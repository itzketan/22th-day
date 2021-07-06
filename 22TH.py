import PyPDF2
mergeFile = PyPDF2.PdfFileMerger()
mergeFile.append(PyPDF2.PdfFileReader('C:\KETAN GURAV\BOOK\matlab.pdf'))
mergeFile.append(PyPDF2.PdfFileReader('C:\KETAN GURAV\BOOK\matlab_basic.pdf'))
mergeFile.write("NewMergedFile.pdf")