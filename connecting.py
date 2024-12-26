import cv2
import numpy as np
from PIL import Image

# Create shifts list
shifts = [0, 21, 30, 30, 30, 32, 20, 30, 30, 31, 20, 30, 30, 19, 7, 0, 31, 34, 32, 22, 30, 31, 30, 32, 21, 32, 31, 31, 22, 29, 17, 0, 0, 0, 0, 0, 30, 20, 31, 30, 30, 31, 21, 30, 30, 30, 21, 30, 31, 30, 21, 30, 21, 9, 0]

# Read first image to get dimensions
filename = f"image_0_0.jpg"
first_image = cv2.imread('cropped/'+filename)
img_height, img_width = first_image.shape[:2]

# Calculate template dimensions
total_width = max(shifts) + (len(shifts) - 1) * 10 + img_width
template = np.zeros((img_height, total_width, 3), dtype=np.uint8)

# Stitch images
for x in range(len(shifts)):
    filename = f"image_{x}_0.jpg"
    image = cv2.imread('cropped/'+filename)
        
    # Calculate position
    x_offset = shifts[x] + x * 10
    
    # Ensure we don't exceed template boundaries
    if x_offset + img_width <= total_width:
        template[:, x_offset:x_offset+img_width] = image

# Save the result
cv2.imwrite('stitched_result.jpg', template)