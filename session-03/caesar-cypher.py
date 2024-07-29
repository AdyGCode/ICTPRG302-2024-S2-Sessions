# --------------------------------------------------------
#
# Caesar Cypher (Mark Anthony version)
#
# Folder:    session-03
# Filename:  caesar-cypher.py
# Author:    Adrian Gould <adrian.gould@nmtafe.wa.edu.au>
# Version:   1.0
# 
# --------------------------------------------------------

print("Welcome to the Caesar Cypher program")

name = input("What is your name")

print(name, "hope you enjoy encrypting and decrypting words.")

letter = input("Please enter a letter to encrypt: ")
shift = input("Shift by how many characters: ")

try:
    shift = int(shift)
except:
    error = input("Invalid value for shift, press ENTER to stop")
    quit()

if letter.isalpha():
    ascii_value = ord(letter)
    ascii_value = ascii_value + shift
    answer = chr(ascii_value)

    print("Caesar cypher letter is", answer)

else:
    print("You did not enter a letter to shift")
