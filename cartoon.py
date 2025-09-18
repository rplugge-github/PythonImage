#https://www.askpython.com/python/examples/images-into-cartoons

import cv2
import numpy as np
import matplotlib.pyplot as plt
import argparse
import os

# Create parser
parser = argparse.ArgumentParser(description="Example script with arguments")

# Default values
default_filename = "images/image.jpg"
_, default_output = os.path.split(parser.prog)
default_output = "images/_" + os.path.splitext(default_output)[0] + "_output.jpg"
default_show = "yes"

# Add arguments
parser.add_argument('-f', "--filename", type=str, default=default_filename,
                    help=f"Input image filename (default {default_filename})")
parser.add_argument('-o', "--output", nargs='?', const=default_output, default=None, 
                    help=f"Output image filename (default {default_output}, if argument without value)")
# Add an argument that can be used with or without a value
parser.add_argument('-s', '--show', nargs='?', const=default_show, default=None, 
                    choices=["yes", "no", "true", "false", "1", "0"],
                    help=f"Show image (default {default_show})")

# Parse arguments
args = parser.parse_args()

# Access the script name
print(f"Script name: {parser.prog}")
print(f"Filename: {args.filename}")
img = cv2.imread(args.filename)
if img is None:
    print("Image not found")
    exit()

# Convert BGR to RGB
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

"""
plt.figure(figsize=(10,10))
plt.imshow(img)
plt.axis("off")
plt.title("Original Image")
plt.show()
"""

# Convert to grayscale and apply median blur
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 5)

"""
plt.figure(figsize=(10,10))
plt.imshow(gray,cmap="gray")
plt.axis("off")
plt.title("Grayscale Image")
plt.show()
"""

# Detect edges using adaptive thresholding
edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

"""
plt.figure(figsize=(10,10))
plt.imshow(edges,cmap="gray")
plt.axis("off")
plt.title("Edged Image")
plt.show()
"""

# Apply bilateral filter to smooth the colors
color = cv2.bilateralFilter(img, 9, 250, 250)
cartoon = cv2.bitwise_and(color, color, mask=edges)
plt.figure(figsize=(10,10))
plt.imshow(cartoon,cmap="gray")
plt.axis("off")
plt.title("Cartoon Image")
#plt.show()

# Save output if output filename is provided
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imsave.html
if not args.output is None:
    plt.imsave(args.output, cartoon,cmap="gray")
    print(f"Output file saved: {args.output}")

# Show image if show argument is provided
show = default_show
if args.show is None:
    print("Show argument not provided.")
elif args.show == default_show:
    print("Show argument provided without a value. Using default:", args.show)
else:
    print("Show argument provided with value:", args.show)
    show = args.show

if show.lower() in ['true', '1', 'yes']:
    print("Show image:", show)
    plt.show()
