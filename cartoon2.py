#https://www.geeksforgeeks.org/blogs/cartooning-an-image-using-opencv-python/

import cv2
import argparse

# Create parser
parser = argparse.ArgumentParser(description="Example script with arguments")

# Default values
default_filename = "image.jpg"
default_output = "image_output.jpg" # Default output filename, if --Output is used without a value
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

# Prep grayscale & blur
g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
g = cv2.medianBlur(g, 5)

# Edges
e = cv2.adaptiveThreshold(g, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                          cv2.THRESH_BINARY, 9, 9)

# Smooth color
c = cv2.bilateralFilter(img, 9, 250, 250)

# Combine
cartoon = cv2.bitwise_and(c, c, mask=e)

# Save output if output filename is provided
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imsave.html
if not args.output is None:
    cv2.imwrite(args.output, cartoon)    
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
    cv2.imshow("Cartoon", cartoon)

cv2.waitKey(0)
cv2.destroyAllWindows()