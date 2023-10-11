import inputer
from inputer import *
import time
import ppChecker
from ppChecker import *



def run():
    time.sleep(0.5)
    down()
    time.sleep(0.5)
    down()
    time.sleep(0.5)
    right()
    time.sleep(0.5)
    a()

def levelUp():
    time.sleep(0.5)
    a()
    time.sleep(0.5)
    a()

def giveUponNewMove():
    time.sleep(0.5)
    down()
    time.sleep(0.5)
    down()
    time.sleep(0.5)
    a()
    time.sleep(4)
    a()

def figt():
    time.sleep(0.5)
    up()
    time.sleep(0.5)
    up()
    time.sleep(0.5)
    a()

def heal():
    time.sleep(0.5)
    down()
    time.sleep(0.5)
    left()
    time.sleep(0.5)
    a()
    time.sleep(0.5)
    a()
    time.sleep(0.5)
    a()
    time.sleep(0.5)
    a()
    time.sleep(0.5)
    a()

def useMove1(lastMove):
    print("use move 1")
    if(lastMove==0):
        time.sleep(0.5)
        a()
        time.sleep(0.5)
        a()
    if(lastMove==1):
        time.sleep(0.5)
        a()
    if(lastMove == 2):
        time.sleep(0.5)
        left()
        time.sleep(0.5)
        a()
    if(lastMove == 3):
        time.sleep(0.5)
        up()
        time.sleep(0.5)
        a()
    if (lastMove == 4):
        time.sleep(0.5)
        up()
        time.sleep(0.5)
        left()
        time.sleep(0.5)
        a()
    return 1

def useMove2(lastMove):
    print("use move 2")
    if(lastMove==0):
        time.sleep(0.5)
        right()
        time.sleep(0.5)
        a()
    if (lastMove == 1):
        time.sleep(0.5)
        right()
        time.sleep(0.5)
        a()
    if (lastMove == 2):
        time.sleep(0.5)
        a()
        time.sleep(0.5)
        a()
    if (lastMove == 3):
        time.sleep(0.5)
        right()
        time.sleep(0.5)
        up()
        time.sleep(0.5)
        a()
    if (lastMove == 4):
        time.sleep(0.5)
        up()
        time.sleep(0.5)
        a()
    return 2

def useMove3(lastMove):
    print("use move 3")
    if(lastMove==0):
        time.sleep(0.5)
        down()
        time.sleep(0.5)
        a()
    if(lastMove==1):
        time.sleep(0.5)
        down()
        time.sleep(0.5)
        a()
    if (lastMove == 2):
        time.sleep(0.5)
        down()
        time.sleep(0.5)
        left()
        time.sleep(0.5)
        a()
    if (lastMove == 3):
        time.sleep(0.5)
        a()
        time.sleep(0.5)
        a()
    if (lastMove == 4):
        time.sleep(0.5)
        left()
        time.sleep(0.5)
        a()
    return 3

def useMove4(lastMove):
    print("use move 4")
    if(lastMove==0):
        time.sleep(0.5)
        down()
        time.sleep(0.5)
        right()
        time.sleep(0.5)
        a()
    if (lastMove == 1):
        time.sleep(0.5)
        down()
        time.sleep(0.5)
        right()
        time.sleep(0.5)
        a()
    if (lastMove == 2):
        time.sleep(0.5)
        down()
        time.sleep(0.5)
        a()
    if (lastMove == 3):
        time.sleep(0.5)
        right()
        time.sleep(0.5)
        a()
    if (lastMove == 4):
        time.sleep(0.5)
        a()
        time.sleep(0.5)
        a()
    return 4

#print(move1Checker())
#print(move2Checker())
#print(move3Checker())
#print(move4Checker())

#time.sleep(4)
#run()

#lastMove =3
#time.sleep(4)
#levelUp()
#time.sleep(8)
#giveUponNewMove()
#figt()
#time.sleep(0.5)
#useMove3()
#heal()