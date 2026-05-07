"""
@fileoverview Menu module for the user prompt.
@package Nisk (OpenCV)
@author Tyree Franklin Jr.
@date 2026-05-06
"""

from grayscale_data import *

print("Welcome to Nisk, an Image Processing Bot :)\n")

def menu():
    grabbing_input = True
    while grabbing_input:
        try:
            s = int(input("Enter 1-5:\n1. Grayscale Data\n2. Split Color Channels\n3. Merge Color Channels\n0. Quit\n\nInput: "))
        except ValueError:
            print("\nValueError: Invalid input type.\n")
        else:
            grabbing_input = False
            return s

running = True

def run(func):
    match func:

        #Grayscale Data Module
        case 1:
            print("\n==========================================\nGrayscale Data")
            file = input("\nEnter the file name: ") 
            grayscale(file)
            
        # End program    
        case 0:
            global running
            running = False


while running:
    func = menu()
    run(func)


"""
Revision History:
1.0 (2026-05-06) - Basic prompting, input exception handling, input validation.
1.01 (2026-05-06) - Successfully calls external grayscale module, and quits upon user's request.
1.02 (2026-05-07) - Minor modifications to the ASCII decorations, and removed uncessesary 'menu()' calls.
"""