import textract
import os
from docx import Document
from docx.shared import Inches

document = Document()
document.save('test.docx')


text = ""
f = open("helloworld.txt", "w")

for filename in os.listdir(os.getcwd()):
    if filename.endswith('.doc'):
        f.write(str(textract.process(filename)))


f.close()

