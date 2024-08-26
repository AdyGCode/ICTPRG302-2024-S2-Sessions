# --------------------------------------------------------
#
# File Read Demo 4
#
# Folder:    session-07
# Filename:  file-read-4.py
# Author:    Adrian Gould <Adrian.Gould@nmtafe.wa.edu.au>
# Version:   0.0
# 
# --------------------------------------------------------

read_handle = open("quick.txt","r")
quick_list = []

for line in read_handle:
    quick_list.append(line.strip())

print(quick_list)
