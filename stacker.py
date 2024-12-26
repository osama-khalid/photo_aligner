import cv2
import numpy as np
from PIL import Image

filename = f"image_0_0.jpg"
first_image = cv2.imread('cropped/'+filename)
img_height, img_width = first_image.shape[:2]

# Calculate template dimensions

template = np.zeros((img_height+(69*10), img_width, 3), dtype=np.uint8)

y_offset = 0
for y in range(0,69):
    filename = f"image_0_{y}.jpg"
    print(filename)
    image = cv2.imread('cropped/'+filename)

    y_offset = y_offset+10
    template[y_offset:y_offset+img_height, 0:img_width] = image

cv2.imwrite('template_vertical.jpg', template)