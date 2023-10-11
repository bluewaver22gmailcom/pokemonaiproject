import inputer
from inputer import *
import time
import PIL.Image
import cv2
from PIL import Image
import glob
import os

def imgageOpener():
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
    return img


#move 1
#print(pix[59, 251])
#print(pix[70, 251])
#move 2
#print(pix[189, 253])
#print(pix[192, 252])
#move 3
#print(pix[59, 315])
#print(pix[89, 316])
#move 4
#m4d = pix[187, 317]
#print(m4d[0])
#m4l = pix[198, 316]
#print(m4l[0])

def battleScreenCheck():
    picture = imgageOpener()
    pix = picture.load()
    m1d = pix[106, 237]
    m2d = pix[149,235]
    m3l = pix[106, 298]
    m4l = pix[151, 299]
    #print(m1d)
    #print(m2d)
    #print(m3l)
    #print(m4l)
    if (m1d[0] == m2d[0] == 247 and m1d[1] == m2d[1] == 239):
        return True

    else:
        return False


def newTurnChecker():
    picture = imgageOpener()
    pix = picture.load()
    m1d = pix[59, 251]
    m2d = pix[189, 253]
    m3l = pix[89, 290]
    m4l = pix[198, 290]
    #print(m1d)
    #print(m2d)
    #print(m3l)
    #print(m4l)
    if(m1d[0]==m2d[0]==m3l[0]==m4l[0]==239):
        return True

    else:
        return False

def newMoveChecker():
    picture = imgageOpener()
    pix = picture.load()
    m1d = pix[59, 251]
    m2d = pix[189, 253]
    m3l = pix[89, 316]
    m4l = pix[198, 316]
    #print(m1d)
    #print(m2d)
    #print(m3l)
    #print(m4l)
    if(m1d[0]==m2d[0]==239 and m3l[0]==m4l[0]==41):
        return True

    else:
        return False

def levelUpChecker():
    picture = imgageOpener()
    pix = picture.load()
    spot1 = pix[200, 70]
    spot2 = pix[200, 100]
    spot3 = pix[200, 130]
    #print(spot1)
    #print(spot3)
    #print(spot2)

    if(spot1[0]==255 and spot2[0]==255 and spot3[0]==255):

        return True

    else:
        return False

def move1Checker():
    picture = imgageOpener()
    pix = picture.load()
    hasPP = True
    m1d = pix[59, 251]
    #print(m1d[0])
    m1l = pix[70, 251]
    #print(m1l[0])
    if(m1l[0]>120 and m1d[0]>120):
        hasPP = False
        return hasPP

    else:
        return hasPP

def move2Checker():
    picture = imgageOpener()
    pix = picture.load()
    hasPP = True
    m2d = pix[189, 253]
    #print(m2d[0])
    m2l = pix[192, 252]
    #print(m2l[0])
    if(m2l[0]>120 and m2d[0]>120):
        hasPP = False
        return hasPP

    else:
        return hasPP

def move3Checker():
    picture = imgageOpener()
    pix = picture.load()
    hasPP = True
    m3d = pix[59, 315]
    #print(m3d[0])
    movechecker3 = pix[30, 300]
    #print(movechecker3[2])
    m3l = pix[89, 316]
    #print(m3l[0])
    if (movechecker3[2] < 120):
        hasPP = False
        return hasPP
    if(m3l[0]>120 and m3d[0]>120):
        hasPP = False
        return hasPP

    else:
        return hasPP

def move4Checker():
    picture = imgageOpener()
    pix = picture.load()
    hasPP = True
    m4d = pix[187, 317]
    movechecker4 = pix[150, 300]
    #print(movechecker4[2])
    #print(m4d[0])
    m4l = pix[198, 316]
    #print(m4l[0])
    if(movechecker4[2]<120):
        hasPP =False
        return hasPP

    if(m4l[0]>120 and m4d[0]>120):
        hasPP = False
        return hasPP

    else:
        return hasPP
#print(move1Checker())
#print(move2Checker())
#print(move3Checker())
#print(move4Checker())
#print(levelUpChecker())
print(battleScreenCheck())