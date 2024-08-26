# --------------------------------------------------------
#
# File Read Demo 11
#
# Folder:    session-07
# Filename:  file-read-11.py
# Author:    Adrian Gould <Adrian.Gould@nmtafe.wa.edu.au>
# Version:   0.0
# 
# --------------------------------------------------------

filename = input('Enter the file name: ')
filehandle = open(filename)
count = 0
for line in filehandle:
    if line.startswith('Subject: '):
        count = count + 1
print('There were', count, 'subject lines in', filehandle)
