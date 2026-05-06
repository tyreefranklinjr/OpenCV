"""
@fileoverview Menu module for the user prompt.
@package Nisk (OpenCV)
@author Tyree Franklin Jr.
@date 2026-05-06
"""

print("Welcome to Nisk, an Image Processing Bot :)")
grabbing_input = True

while grabbing_input:
    try:
        s = int(input("Enter 1-5: "))

    except ValueError:
        print("\nValueError: Invalid input type.\n")

    else:
        grabbing_input = False


"""
Revision History:
1.0 (2026-05-06) - Basic prompting, input exception handling, input validation.
"""