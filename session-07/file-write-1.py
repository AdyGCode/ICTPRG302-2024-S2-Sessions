# --------------------------------------------------------
#
# File Write Demo 1
#
# Folder:    session-07
# Filename:  file-write-1.py
# Author:    Adrian Gould <Adrian.Gould@nmtafe.wa.edu.au>
# Version:   0.0
# 
# --------------------------------------------------------

write_handle = open('players.txt', 'w')

write_handle.write('DinoShark\nMouseDragon')
write_handle.write('MonkeyHorse\nPandaShrew')

write_handle.close()
