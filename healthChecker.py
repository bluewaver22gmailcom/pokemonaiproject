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

def healthCheck118():
    picture = imgageOpener()
    pix = picture.load()
    haslessthan30health = 0
    thirtypercent = pix[214, 118]
    print(thirtypercent[1])
    print(thirtypercent)
    if(thirtypercent[1]>210):
        return 1
    if (thirtypercent[1] < 210 and thirtypercent[1] > 50):
        return 2
    if (thirtypercent[1] < 50):
        return 3

def healthCheck119():
    picture = imgageOpener()
    pix = picture.load()
    haslessthan30health = 0
    thirtypercent = pix[214, 119]
    print(thirtypercent[1])
    print(thirtypercent)
    if (thirtypercent[1] > 210):
        return 1
    if (thirtypercent[1] < 210 and thirtypercent[1] > 50):
        return 2
    if (thirtypercent[1] < 50):
        return 3

def healthCheck120():
    picture = imgageOpener()
    pix = picture.load()
    haslessthan30health = 0
    thirtypercent = pix[214, 120]
    print(thirtypercent[1])
    print(thirtypercent)
    if (thirtypercent[1] > 210):
        return 1
    if (thirtypercent[1] < 210 and thirtypercent[1] > 50):
        return 2
    if (thirtypercent[1] < 50):
        return 3

def healthCheck121():
    picture = imgageOpener()
    pix = picture.load()
    haslessthan30health = 0
    thirtypercent = pix[214, 121]
    print(thirtypercent[1])
    print(thirtypercent)
    if (thirtypercent[1] > 210):
        return 1
    if (thirtypercent[1] < 210 and thirtypercent[1] > 50):
        return 2
    if (thirtypercent[1] < 50):
        return 3

def healthCheck():
    lessthan30 = True
    if(healthCheck118()==2 or healthCheck119()==2 or healthCheck120()==2 or healthCheck121()==2):
        lessthan30 = False
    return lessthan30


#print(healthCheck())
