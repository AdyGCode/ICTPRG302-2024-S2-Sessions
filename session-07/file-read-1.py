# --------------------------------------------------------
#
# Read File Demo 1
#
# Folder:    session-07
# Filename:  file-read-1.py
# Author:    Adrian Gould <Adrian.Gould@nmtafe.wa.edu.au>
# Version:   0.0
# 
# --------------------------------------------------------

read_handle = open("quick.txt", "r")
quick_text = read_handle.read()
print(quick_text)
