

from pdf2docx import Converter
PdfFile = r"D:\MY FILES\Foreign Work Process\FOREIGN FOR RP\DEFECTS OR OBJECTIONS\Atta Ullah Afridi.pdf"
#PdfFile2= open(r"Atta Ullah Afridi.pdf")
DocxFile = r"D:\MY FILES\Foreign Work Process\FOREIGN FOR RP\DEFECTS OR OBJECTIONS\Atta Ullah convert3.docx"
convertFile = Converter(PdfFile)
convertFile.convert(DocxFile)
convertFile.close()
