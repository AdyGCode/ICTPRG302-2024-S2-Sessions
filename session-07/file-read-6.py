# --------------------------------------------------------
#
# File Read Demo 6
#
# Folder:    session-07
# Filename:  file-read-4.py
# Author:    Adrian Gould <Adrian.Gould@nmtafe.wa.edu.au>
# Version:   0.0
# 
# --------------------------------------------------------

read_handle = open("numbers.txt","r")
number_list = []

for line in read_handle:
    number_list.append(int(line.strip()))

print(number_list)
