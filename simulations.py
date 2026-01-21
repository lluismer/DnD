#Import all functions from dice roll
from dice_roll import *
import matplotlib.pyplot as plt


def roll_list(faceNum,testNum = 100000,diceMod=0,toBeat=0):
    roll_list = []
    if toBeat != 0:
        wins = 0
        for i in range(testNum):
            num = dice_roll(faceNum) + diceMod
            roll_list.append(num)
            if num > toBeat:
                wins += 1
        return [roll_list,wins]
    else:  
        for i in range(testNum):
            num = dice_roll(faceNum) + diceMod
            roll_list.append(num)      
        return [roll_list]

def average(r_list: list):
    return sum(r_list)/len(r_list)

def median(r_list: list):
    r_list = sorted(r_list)
    if len(r_list)%2 == 1:
        return r_list[len(r_list)//2]
    return (r_list[(len(r_list)//2)-1] + r_list[len(r_list)//2])/2

def roll_histogram(faceNum,testNum=100000):
    r_list = roll_list(faceNum,testNum)[0]
    plt.hist(r_list, bins= range(1,faceNum+2), edgecolor="black", linewidth=1, alpha=0.85)
    plt.xticks(range(1, faceNum+1))
    plt.show()

def probabilityOfBeatingAC(diceMod,AC):
    r_list = roll_list(20,diceMod=diceMod,toBeat=AC)
    return r_list[1]/len(r_list[0])

def avgDmg(dmgDice,testNum = 100000):
    #dmgDice has to be a list with three variables; the first one is number of dice, the second the face of the dice

    dmg_list = []
    for i in range(testNum):
        dmg_list.append(multiple_rolls(dmgDice[0],dmgDice[1]) + dmgDice[2])
    return average(dmg_list)

    
def higherAvgDmg(diceMod1,diceMod2, dmgDice1: list,dmgDice2: list,AC):
    # dmgDice has to be a list with three variables; the first one is number of dice,
    # the second the face of the dice, and the third one being the dmg bonus


    prob_hit1 = probabilityOfBeatingAC(diceMod1,AC)
    prob_hit2 = probabilityOfBeatingAC(diceMod2,AC)
    avg_dmg1 = avgDmg(dmgDice1)
    avg_dmg2 = avgDmg(dmgDice2)

    dmgXturn1 = prob_hit1 * avg_dmg1
    dmgXturn2 = prob_hit2 * avg_dmg2

    return [dmgXturn1,dmgXturn2]

print(higherAvgDmg(7,8,[2,10,0],[2,6,5],16))