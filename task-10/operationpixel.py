import cv2
import os
from PIL import Image, ImageDraw

def detectdot(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY_INV)
    
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    if len(contours) == 0:
        return None, None 

    contour = max(contours, key=cv2.contourArea)
    M = cv2.moments(contour)
    
    if M["m00"] == 0:
        return None, None 
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])
    
    color = image[cY, cX]

    
    color_rgb = (color[2], color[1], color[0])

    
    if color_rgb == (0, 0, 255):  
        color_rgb = (255, 255, 0) 
    
    return (cX, cY), color_rgb

def sortimages(images):
    import re

    def extractnumber(filename):
        match = re.search(r'(\d+)', filename)
        return int(match.group(0)) if match else float('inf')  

    return sorted(images, key=extractnumber)

def stitchimages(image_folder):
    images = [img for img in os.listdir(image_folder) if img.endswith('.png')]
    images = sortimages(images)


    stitchedimage = Image.new('RGB', (512, 512), (255, 255, 255))  
    draw = ImageDraw.Draw(stitchedimage)
    
    last_position = None
    last_color = None
    
    for img_name in images:
        img_path = os.path.join(image_folder, img_name)
        
        position, color = detectdot(img_path)
        if position is None:
            last_position = None
            last_color = None
            continue
        
        if last_position is not None:

            draw.line([last_position, position], fill=color, width=5)
        
        last_position = position
        last_color = color
    
    output_path = os.path.join(image_folder, 'image.png')
    stitchedimage.save(output_path)
    print(f"Stitched image saved as {output_path}")

image_folder = '/home/kanju/Operation-Pixel-Merge/assets'  
stitchimages(image_folder)
