# --------------------------------------------------------
#
# Read File Demo 3
#
# Folder:    session-07
# Filename:  file-read-1.py
# Author:    Adrian Gould <Adrian.Gould@nmtafe.wa.edu.au>
# Version:   0.0
# 
# --------------------------------------------------------

read_handle = open("quick.txt", "r")
quick_list = read_handle.readlines()
print(quick_list)
