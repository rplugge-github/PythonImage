#https://www.askpython.com/python/examples/images-into-cartoons

import cv2
import numpy as np
import matplotlib.pyplot as plt
import argparse

# Create parser
parser = argparse.ArgumentParser(description="Example script with arguments")

# Add arguments
parser.add_argument("--filename", type=str, help="Image filename", default="image.jpg")
#parser.add_argument("--age", type=int, help="Your age")

# Parse arguments
args = parser.parse_args()

print(f"Filename: {args.filename}")
img = cv2.imread(args.filename)
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

"""
plt.figure(figsize=(10,10))
plt.imshow(img)
plt.axis("off")
plt.title("Original Image")
plt.show()
"""

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 5)

"""
plt.figure(figsize=(10,10))
plt.imshow(gray,cmap="gray")
plt.axis("off")
plt.title("Grayscale Image")
plt.show()
"""

edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

"""
plt.figure(figsize=(10,10))
plt.imshow(edges,cmap="gray")
plt.axis("off")
plt.title("Edged Image")
plt.show()
"""

color = cv2.bilateralFilter(img, 9, 250, 250)
cartoon = cv2.bitwise_and(color, color, mask=edges)
plt.figure(figsize=(10,10))
plt.imshow(cartoon,cmap="gray")
plt.axis("off")
plt.title("Cartoon Image")
plt.show()