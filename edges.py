import cv2
import numpy as np
from PIL import Image

def find_black_edges(img):
    # Convert to grayscale if not already
    if len(img.shape) == 3:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    else:
        gray = img
        
    # Convert to binary (black and white)
    _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    
    # Find leftmost and rightmost black pixels for each row
    left_edges = []
    right_edges = []
    for row in binary:
        # Find indices where pixels are black (0)
        black_pixels = np.where(row == 0)[0]
        if len(black_pixels) > 0:
            left_edges.append(black_pixels[0])
            right_edges.append(black_pixels[-1])
    
    # Return the overall leftmost and rightmost edges if found
    left_edge = min(left_edges) if left_edges else None
    right_edge = max(right_edges) if right_edges else None
    return left_edge, right_edge

filename = f"image_0_0.jpg"
first_image = cv2.imread('cropped/'+filename)
img_height, img_width = first_image.shape[:2]

# Calculate template dimensions
template = np.zeros((img_height+(69*10), img_width, 3), dtype=np.uint8)

y_offset = 0

for y in range(0,69):
    filename = f"image_51_{y}.jpg"
    
    image = cv2.imread('cropped/'+filename)
    
    # Convert to black and white and find edges
    if image is not None:
        left_edge, right_edge = find_black_edges(image)
        if left_edge is not None and right_edge is not None:
            print(f"{filename}: Left edge = {left_edge}, Right edge = {right_edge}")
            