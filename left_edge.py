import cv2
import numpy as np
from PIL import Image

def find_leftmost_black_edge(img):
    # Convert to grayscale if not already
    if len(img.shape) == 3:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    else:
        gray = img
        
    # Convert to binary (black and white)
    _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    
    # Find leftmost black pixel for each row
    leftmost_edges = []
    for row in binary:
        # Find indices where pixels are black (0)
        black_pixels = np.where(row == 0)[0]
        if len(black_pixels) > 0:
            leftmost_edges.append(black_pixels[0])
    
    # Return the overall leftmost edge if found
    return min(leftmost_edges) if leftmost_edges else None

filename = f"image_0_0.jpg"
first_image = cv2.imread('cropped/'+filename)
img_height, img_width = first_image.shape[:2]

# Calculate template dimensions
template = np.zeros((img_height+(69*10), img_width, 3), dtype=np.uint8)

y_offset = 0

for y in range(0,69):
    filename = f"image_51_{y}.jpg"
    #print(filename)
    image = cv2.imread('cropped/'+filename)
    
    # Convert to black and white and find edge
    if image is not None:
        leftmost_edge = find_leftmost_black_edge(image)
        if leftmost_edge is not None:
            print(f"Leftmost black edge in {filename}: {leftmost_edge}")