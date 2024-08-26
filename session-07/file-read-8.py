# --------------------------------------------------------
#
# File Read Demo 8 (Searching)
#
# Folder:    session-07
# Filename:  file-read-8.py
# Author:    Adrian Gould <Adrian.Gould@nmtafe.wa.edu.au>
# Version:   0.0
# 
# --------------------------------------------------------

filehandle = open("mbox-short.txt", "r")
for line in filehandle:
    if line.startswith("From:"):
        line = line.rstrip()
        print(line)
