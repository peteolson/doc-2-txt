import re
import os
import sys
import docx
from subprocess import Popen, PIPE


os.system('antiword ' + "AppleDip.doc" + ' > ' + "AppleDip" + '.txt')
#text = os.system('antiword '+ "AppleDip.doc")
os.system('antiword '+ "AppleDip.doc")

def getText(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)

#print(getText("bakedFish.docx"))

def document_to_text(filename):
    if filename[-4:] == ".doc":
        cmd = ['antiword']
        p = Popen(cmd, stdout=PIPE)
        stdout, stderr = p.communicate()
    return stdout.decode('ascii', 'ignore')
#print(document_to_text("appleDip.doc"))