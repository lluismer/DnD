#Where all the probability and dice rolls happens
#Libraries
import random

def dice_roll(faceNum):
    return random.randint(1,faceNum)

def d4():
    return dice_roll(4)

def d6():
    return dice_roll(6)

def d8():
    return dice_roll(8)

def d10():
    return dice_roll(10)

def d12():
    return dice_roll(12)

def d20():
    return dice_roll(20)

def d00():
    return dice_roll(100)//10

dices = {4:d4,6:d6,8:d8,10:d10,12:d12,20:d20,00:d00}

def multiple_rolls(rollNum,faceNum):
    if(rollNum <= 0):
        return 0
    return dices[faceNum]() + multiple_rolls(rollNum - 1, faceNum)