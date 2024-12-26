import requests
import os

# Create a directory to save images
output_dir = "downloaded_images_2"
os.makedirs(output_dir, exist_ok=True)

# Loop through the ranges
for y in range(0, 71):
    for x in range(0, 56):
    
        # Construct the URL
        url = f'http://magnifier.flashphotography.com/MagnifyRender.ashx?X={x*10}&Y={y*10}&+=700&O=27251902&R=00003&F=0214&A=71714'
        # File name based on x and y
        filename = f"image_{x}_{y}.jpg"
        filepath = os.path.join(output_dir, filename)
        try:
            # Send the request
            response = requests.get(url, stream=True)
            # Check if the request was successful
            if response.status_code == 200:
                # Save the image
                with open(filepath, 'wb') as f:
                    for chunk in response.iter_content(1024):
                        f.write(chunk)
                print(f"Downloaded {filename}")
            else:
                print(f"Failed to download {filename}: {response.status_code}")
        except Exception as e:
            print(f"Error downloading {filename}: {e}")
