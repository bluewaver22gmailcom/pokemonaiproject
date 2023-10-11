import pytesseract
import PIL.Image
import cv2
from PIL import Image
import glob
import os
import time




def pokemonRecognize():

    myconfig = r"--psm 8 --oem 3"
    mrt = 0
    mrf = " "
    name = " "


    for files in os.listdir(r"C:\Users\bluew\OneDrive\Documents\pokemon ai project\desmume\Screenshots"):
        # print(r"C:/Users/bluew/OneDrive/Documents/pokemon ai project/desmume/Screenshots/" + files)
        # img = Image.open(r"C:/Users/bluew/OneDrive/Documents/pokemon ai project/desmume/Screenshots/" + files)
        c_time = os.path.getctime(r"C:/Users/bluew/OneDrive/Documents/pokemon ai project/desmume/Screenshots/" + files)
        # print(c_time)
        if (c_time > mrt):
            mrt = c_time
            mrf = files
        # print(mrt)
        # print(mrf)

    img = Image.open(r"C:/Users/bluew/OneDrive/Documents/pokemon ai project/desmume/Screenshots/" + mrf)
    imgCropped = img.crop(box=(0, 24, 65, 40))
    nameRaw = pytesseract.image_to_string(imgCropped, config=myconfig)
    name = nameRaw.strip()
    return name

def grassresist(Name):

    grassResist = False

    if Name == 'STARLY':
        grassResist = True

    if (Name == "CHIMCHAR"):
        grassResist = True

    if (Name == 'BIDOOF'):
        grassResist = False

    if (Name == 'KRICKETOT'):
        grassResist = True

    if (Name == 'SHINX' or Name == 'SHIN'):
        grassResist = False

    if (Name == 'ZUBAT'):
        grassResist = True

    if (Name == 'BURMY' or Name == "BURMY ="):
        grassResist = True

    if (Name == 'ABRA'):
        grassResist = False

    if (Name == 'BUDEW'):
        grassResist = True

    if (Name == 'MACHOP'):
        grassResist = False

    if (Name == 'GEODUDE'):
        grassResist = False

    if (Name == 'ONIX'):
        grassResist = False

    if (Name == 'CRANIDOS'):
        grassResist = False

    if (Name == 'WURMPLE'):
        grassResist = True

    return grassResist



#moveRecognize()

#print(pokemonRecognize())
#print(grassresist(pokemonRecognize()))
#print(grassResist)
#img.show(imgCropped)

#img = Image.open(r'C:\Users\bluew\OneDrive\Documents\pokemon ai project\desmume\Screenshots\3541 - Pokemon Platinum Version (US)(XenoPhobia)__22336.png')
#deez = os.path.getctime(r'C:\Users\bluew\OneDrive\Documents\pokemon ai project\desmume\Screenshots')
#print(deez)
#path = r'C:\Users\bluew\OneDrive\Documents\pokemon ai project\desmume\Screenshots/1.png'
#c_time = os.path.getctime(path)
#list_of_files = glob.glob(r'C:/Users/bluew/OneDrive/Documents/pokemon ai projec/desmume/Screenshots/*.png') # * means all if need specific format then *.csv
#print(list_of_files)
#latest_file = max(files, key=os.path.getctime)
#print(latest_file)
#myconfig = r"--psm --oem"
#1imgCropped = img.crop(box = (14,230,112,245))
#2imgCropped = img.crop(box = (142,230,241,245))
#3imgCropped = img.crop(box = (15,295,113,310))
#4imgCropped = img.crop(box = (142,295,241,310))
#reader = easyocr.Reader(['en'])
#pipeline = keras_ocr.pipeline.Pipeline()
#img = Image.open(r"C:\Users\bluew\OneDrive\Documents\pokemon ai project\desmume\Screenshots\3541 - Pokemon Platinum Version (US)(XenoPhobia)__18239.png")
#imgCropped = img.crop(box = (142,295,241,310))
#imgCropped.show(imgCropped)

#imgCropped.save(r"C:\Users\bluew\OneDrive\Documents\pokemon ai project\desmume\Screenshots\1.png")
#time.sleep(2)
#images = [keras_ocr.tools.read(img) for img in['2.png']]
#print(images)
#results = pipeline.recognize(r"C:\Users\bluew\OneDrive\Documents\pokemon ai project\desmume\Screenshots\1.png")

#results = reader.readtext(r"C:\Users\bluew\OneDrive\Documents\pokemon ai project\desmume\Screenshots\1.png")
#print(results)
#moveName = pytesseract.image_to_string(imgCropped, lang='eng')
#print(moveName)