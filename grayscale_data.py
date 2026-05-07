"""
@fileoverview Gray scale module to process the functionality traits.
@package Nisk (OpenCV)
@author Tyree Franklin Jr.
@date 2026-05-07
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

def grayscale(file):

   
    image = cv2.imread(file, 0)
    
    if image is None:
        print(f"FileError:n {file} is not in the directory.")
    else:
        print(f"\n{image}\n\n")

    print()

"""
Revision History:
1.0 (2026-05-07) - Initial commit, deployed 'imread' function and exception error handling.
"""