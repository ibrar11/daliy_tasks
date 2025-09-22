import os

# importing os module 
filePath = '/Users/macbook/Downloads/subs.json'

""" Open the file and get
the file descriptor associated
with it using os.open() method"""
fd = os.open(filePath, os.O_RDONLY)

""" Read at most n bytes 
from file descriptor fd
using os.read() method"""
content = os.read(fd, 50)

#print the read content
print(content)

#closed the file
os.close(fd)