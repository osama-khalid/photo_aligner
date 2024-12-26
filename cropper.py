import cv2
import numpy as np

from PIL import Image

def extract_center_box(image_path, output_path, box_size=116):
    # Open the image
    img = Image.open(image_path)
    
    # Get original image dimensions
    width, height = img.size
    
    # Calculate coordinates for the centered box
    left = (width - box_size) // 2
    top = (height - box_size) // 2
    right = left + box_size
    bottom = top + box_size
    
    # Crop the image
    cropped_img = img.crop((left, top, right, bottom))
    
    # Save the cropped image
    cropped_img.save(output_path)
    
    # Close the images
    img.close()
    cropped_img.close()

# Usage
X=[]
x2 = []
y2 = []
Y = []
import os 
import tqdm
for filename in tqdm.tqdm(os.listdir('downloaded_images/')):
    if filename.endswith('.jpg'):
        extract_center_box('downloaded_images/'+filename, 'cropped/'+filename)