"""
f = open('helloworld.txt','a')
f.write('hello world')
f.close()
"""


file = open('file-to-read.txt', 'r')
for line in file:
    print(line)

