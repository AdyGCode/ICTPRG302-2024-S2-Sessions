# --------------------------------------------------------
#
# Demo Temperature Converter
#
# Folder:    session-04
# Filename:  demo_temp_convert_v2.py
# Author:    Adrian Gould <adrian.gould@nmtafe.wa.edu.au>
# Version:   1.0
# 
# --------------------------------------------------------

def welcome():
    print("-" * 60)
    print("Hello and welcome to Temperature Converter")
    print("-" * 60)
    print()


def get_scale():
    while True:
        scale = input("From (C) Celsius or (F) Fahrenheit?")
        scale = scale.upper()
        if scale == "C" or scale == "F":
            break
        print("ERROR: Unknown Scale, use C or F only.")
    return scale


def get_temperature():
    while True:
        original_temperature = input("Enter the temperature: ")
        try:
            original_temperature = float(original_temperature)
        except:
            print("ERROR: Please enter a numeric value.")
        else:
            break
    return original_temperature

def display_results(scale, temperature):
    if scale == "C":
        # Calculate Fahrenheit
        converted_temperature = (temperature * 9 / 5) + 32
        print(converted_temperature)
    elif scale == "F":
        # Calculate Celsius
        converted_temperature = (temperature - 32) * 5 / 9
        print(converted_temperature)
    else:
        # Display "OOPS we did not expect this" error
        print("ERROR! Unknown Error!")


welcome()
from_scale = get_scale()
from_temperature = get_temperature()
display_results(from_scale, from_temperature)