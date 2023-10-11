import inputer
from inputer import *
import pokemonRecognizer
from pokemonRecognizer import *
import moveUser
from moveUser import *
import healthChecker
from  healthChecker import *
import ppChecker
from ppChecker import *
import pokemonRecognizer
from pokemonRecognizer import *
import time

def startMove(lastmoveused):
    #lastmoveused = 0
    time.sleep(0.5)
    screenshot()
    time.sleep(0.75)
    pokemon =pokemonRecognize()
    print(pokemon)
    if(grassresist(pokemon)==True):
        print("grassresist true")
        time.sleep(0.5)
        figt()
        time.sleep(3)
        screenshot()

        if(move1Checker()==True):
            lastmoveused = useMove1(lastmoveused)
            return lastmoveused

        if(move4Checker()==True):
            lastmoveused = useMove4(lastmoveused)
            return lastmoveused

        if(move3Checker()==True):
            lastmoveused = useMove3(lastmoveused)
            return lastmoveused

        if (move2Checker() == True):
            lastmoveused = useMove2(lastmoveused)
            return lastmoveused

    if(grassresist(pokemonRecognize())==False):
        print("grassresist false")
        time.sleep(0.5)
        figt()
        time.sleep(3)
        screenshot()

        if (move4Checker() == True):
            lastmoveused = useMove4(lastmoveused)
            return lastmoveused

        if (move3Checker() == True):
            lastmoveused = useMove3(lastmoveused)
            return lastmoveused

        if (move1Checker() == True):
            lastmoveused = useMove1(lastmoveused)
            return lastmoveused

        if (move2Checker() == True):
            lastmoveused = useMove2(lastmoveused)
            return lastmoveused

    return lastmoveused

def useMove(lastmoveused):
    #lastmoveused = 0
    time.sleep(0.5)
    screenshot()
    time.sleep(0.75)
    pokemon =pokemonRecognize()
    print(pokemon)
    if(grassresist(pokemon)==True):
        print("grassresist true")
        time.sleep(3)
        screenshot()

        if(move1Checker()==True):
            lastmoveused = useMove1(lastmoveused)
            return lastmoveused

        if(move4Checker()==True):
            lastmoveused = useMove4(lastmoveused)
            return lastmoveused

        if(move3Checker()==True):
            lastmoveused = useMove3(lastmoveused)
            return lastmoveused

        if (move2Checker() == True):
            lastmoveused = useMove2(lastmoveused)
            return lastmoveused

    if(grassresist(pokemonRecognize())==False):
        print("grassresist false")
        time.sleep(3)
        screenshot()

        if (move4Checker() == True):
            lastmoveused = useMove4(lastmoveused)
            return lastmoveused

        if (move3Checker() == True):
            lastmoveused = useMove3(lastmoveused)
            return lastmoveused

        if (move1Checker() == True):
            lastmoveused = useMove1(lastmoveused)
            return lastmoveused

        if (move2Checker() == True):
            lastmoveused = useMove2(lastmoveused)
            return lastmoveused

    return lastmoveused

deez = 0
lastmove=0
while(deez==0):
    print(lastmove)
    time.sleep(3)
    screenshot()
    time.sleep(2)
    if(levelUpChecker()==True):
        time.sleep(0.5)
        levelUp()
        time.sleep(8)
        screenshot()
        time.sleep(3)
        if(newMoveChecker()==True):
            time.sleep(0.5)
            giveUponNewMove()
            time.sleep(8)


    if(newTurnChecker()==True):
        nextmove=lastmove
        lastmove=startMove(nextmove)

    if (battleScreenCheck() == True and newTurnChecker()==False):
        nextmove = lastmove
        lastmove = useMove(nextmove)

    if (newMoveChecker() == True):
        time.sleep(0.5)
        giveUponNewMove()
        time.sleep(8)

#time.sleep(4)
#startMove(1)