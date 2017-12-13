"""
f = open('helloworld.txt','a')
f.write('hello world')
f.close()
"""


file = open('file-to-read.txt', 'r')
s = file.read()

f = open('helloworld.txt','a')
f.write(s)
f.close()

