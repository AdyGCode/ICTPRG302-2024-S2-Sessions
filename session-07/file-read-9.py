# --------------------------------------------------------
#
# File Read Demo 9 (Searching)
#
# Folder:    session-07
# Filename:  file-read-8.py
# Author:    Adrian Gould <Adrian.Gould@nmtafe.wa.edu.au>
# Version:   0.0
# 
# --------------------------------------------------------

filehandle = open("mbox-short.txt", "r")
for line in filehandle:
    if not '@uct.ac.za' in line:
        continue
    line = line.rstrip()
    print(line)

