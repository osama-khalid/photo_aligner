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
    #cropped_img.save(output_path)
    
    # Close the images
    img.close()
    cropped_img.close()

# Usage
X={}
x2 = []
y2 = []
Y = {}

import os
import tqdm
for filename in os.listdir('cropped/'):
    for filename_2 in os.listdir('cropped/'):    
        i1,j1=filename.strip('.jpg').split('_')[1:3]
        i2,j2=filename_2.strip('.jpg').split('_')[1:3]
        if i1==i2 and int(j2)-int(j1)==1:
            print(filename,filename_2)
        
    
            image1 = cv2.imread('cropped/'+filename)
            image2 = cv2.imread('cropped/'+filename_2)
            # Get dimensions of image2
            height, width = image2.shape[:2]

            # Calculate coordinates for the 50x50 centered box
            box_size = 80
            left = (width - box_size) // 2
            top = (height - box_size) // 2
            right = left + box_size
            bottom = top + box_size

            # Crop image2 to 50x50
            image2_cropped = image2[top:bottom, left:right]

            image2_cropped

            reference = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
            shift = cv2.cvtColor(image2_cropped, cv2.COLOR_BGR2GRAY)

            _, reference_bw = cv2.threshold(reference, 127, 255, cv2.THRESH_BINARY)
            _, shift_bw = cv2.threshold(shift, 127, 255, cv2.THRESH_BINARY)

            

            # Get dimensions
            h1, w1 = reference_bw.shape  # dimensions of the larger image
            h2, w2 = shift_bw.shape  # dimensions of the smaller image
            dic = {}

            # Calculate valid ranges for x and y positions
            x_range = w1 - w2 + 1
            y_range = h1 - h2 + 1

            # Iterate through all valid positions
            for y in range(y_range):
                for x in range(x_range):
                    # Extract the region from reference_bw that matches image2_bw's size
                    region = reference_bw[y:y+h2, x:x+w2]
                    
                    # Calculate dot product (element-wise multiplication) and take mean
                    dot_product = np.mean(region * shift_bw)
                    
                    # Store coordinates and dot product result
                    dic[(x,y)] = dot_product

            # Find position with maximum dot product
            max_pos = max(dic.items(), key=lambda x: x[1])
            #print(f"Best match position: {max_pos[0]}, Score: {max_pos[1]}")
            print(filename,filename_2,max_pos[0])
            if i1 not in X:
                X[i1] = {}
            if i1 not in Y:
                Y[i1] = {}
            X[i1][j1]=(max_pos[0][0])
            Y[i1][j1]=(max_pos[0][1])

'''
import matplotlib.pyplot as plt

plt.plot(Y[0:200])

plt.show()
# Compare this snippet from images.py:
'''