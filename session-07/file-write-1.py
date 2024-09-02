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

# We need to write a \n (Newline) after each entry as
# .write does not append a newline
write_handle.write('DinoShark\nMouseDragon\n')
write_handle.write('MonkeyHorse\nPandaShrew\n')

write_handle.close()
