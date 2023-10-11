import pytesseract
import os
import PIL.Image
import cv2
from PIL import Image

myconfig = r"--psm 8 --oem 3"
img = Image.open(r'C:\Users\bluew\OneDrive\Documents\pokemon ai project\desmume\Screenshots\3541 - Pokemon Platinum Version (US)(XenoPhobia)__20648.png')
imgCropped = img.crop(box=(33, 167,70, 185))
imgCropped.show(imgCropped)
nameRaw = pytesseract.image_to_string(imgCropped, config=myconfig)
name = nameRaw.strip()
print(name)
