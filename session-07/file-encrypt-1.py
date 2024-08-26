# --------------------------------------------------------
#
# File Read and Encrypt Demo
#
# Folder:    session-07
# Filename:  file-encrypt-1.py
# Author:    Adrian Gould <Adrian.Gould@nmtafe.wa.edu.au>
# Version:   0.0
# 
# --------------------------------------------------------

def welcome():
    '''
    Welcome message
    '''
    print("Welcome to the Caesar Cypher program")
    name = input("Enter your name: ")
    print(name, " - hope you enjoy encrypting and decrypting")
    return name


def get_input_filename():
    '''
    Obtain the filename of the file to be encrypted/decrypted
    '''
    while True:
        print()
        print("#" * 64)
        print("# Please enter the filename to encrypt/decrypt #")
        print("# Enter Q to quit                              #")
        print("#" * 64)
        filename = input("Enter filename:")
        if "Q" == filename.upper():
            quit()
        try:
            file_handle = open(filename, "r")
            return file_handle
        except:
            print("The file does not exist... Please try again.")


def get_output_filename():
    '''
    Obtain the filename to write the encrypted/decrypted data to
    '''
    while True:
        print()
        print("#" * 64)
        print("# Please enter the filename write to           #")
        print("# or enter Q to quit                           #")
        print("#" * 64)
        filename = input("Enter filename:")
        if "Q" == filename.upper():
            print("Terminating program...")
            quit()
        if "" == filename:
            print("No filename given. Please try again.")
        else:
            output_file_handle = open(filename, "w")
            return output_file_handle, filename


def validate_input_file(prefix):
    '''
    Check if the file's first line contains encrypt/decrypt indicator
    - line structure: identifier shift_value
    - identifier:     e = encrypt, d= decrypt
    - shift_value:    integer value
    '''
    prefix = prefix.lower()
    try:
        shift = int(prefix[1:].strip())
    except ValueError:
        message = f"Shift {prefix[1:]} is not a number. Unable to encrypt/decrypt"
    else:
        if prefix[0] in 'ed':
            indicator = prefix[0]
            return indicator, shift
        else:
            message = "Cannot Encrypt/Decrypt data due to invalid input"
    print(message)
    print("Program terminating...")
    quit()


def encrypt(shift, line):
    '''
    Encrypt the message line
    '''

    message = ""
    for letter in line:
        new_character = ord(letter) + shift
        message = message + chr(new_character)
    return message


def decrypt(shift, line):
    '''
    Decrypt the line of data
    '''
    return encrypt(-shift, line)


def main():
    first_line = True
    name = welcome()
    encrypt_file_handle = get_input_filename()

    for line in encrypt_file_handle:
        if first_line is True:
            first_line = False
            encrypt_indicator, shift = validate_input_file(line)
            output_file, output_filename = get_output_filename()

            if encrypt_indicator == "e":
                output_file.write(f"d {shift}\n")

            elif encrypt_indicator == "d":
                output_file.write(f"e {shift}\n")

        else:
            line = line.strip()
            if encrypt_indicator == "e":
                message = encrypt(shift, line)

            else:
                message = decrypt(shift, line)

            output_file.write(f"{message}\n")

    output_file.close()

    print()
    print(f"{name}, your file: {output_filename} was successfully created.")


main()
