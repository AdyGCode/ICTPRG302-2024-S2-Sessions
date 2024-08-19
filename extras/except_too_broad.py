# --------------------------------------------------------
#
# ADD PROGRAM TITLE HERE
#
# ADD SUMMARY OF PROGRAM HERE
#
# Folder:    extras
# Filename:  except_too_broad.py
# Author:    Adrian Gould <Adrian.Gould@nmtafe.wa.edu.au>
# Version:   0.0
# 
# --------------------------------------------------------


value = input("Enter number:")
try:
    value = int(value)
except:
    # Bare except gives PyCharm hint
    # ICTPRG302 will only use this version of except.
    #
    # Adrian indicated that except ValueError
    # would be more 'precise' and used in later units.
    print("ERROR! Not a number")

