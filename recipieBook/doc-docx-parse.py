import textract
import docx
import glob
import os
import subprocess
from subprocess import Popen, PIPE, call

#os.system('antiword ' + filename + ' > ' + filename+'.txt')

header = '<?xml version="1.0"?><tbl_recipies>'
str1 = "<recipies><id></id><date></date>"
str2 = "<note>0</note><archive>0</archive><ingredient>"
str3 = "</ingredient><method></method><meal_list>0</meal_list></recipies>"
footer = '<tbl_recipies>'

f = open('recipie-doc.xml','a')

for filename in os.listdir(os.getcwd()):
    if filename.endswith('.doc'):

        subprocess.call(['soffice', '--headless', '--convert-to', 'docx', filename])


def getText(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)





#text2 = textract.process("AppleDip.doc", encoding='ascii')
num = 530


for filename in os.listdir(os.getcwd()):
    if filename.endswith('.docx'):

        num += 1
        f.write("<recipies><id>"
            + str(num)
            + "</id><date></date>"
            + "<name>"
            + os.path.splitext(filename)[0]
            + "</name>"
            + str2
            + getText(filename)
            + str3)

f.close()

"""

"""

