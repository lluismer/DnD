#Import all functions from dice roll
from dice_roll import *
import matplotlib.pyplot as plt


def roll_list(testNum,faceNum):
    roll_list = []
    for i in range(testNum):
        roll_list.append(dice_roll(faceNum))
    return roll_list

def average(r_list: list):
    return sum(r_list)/len(r_list)

def median(r_list: list):
    r_list = sorted(r_list)
    if len(r_list)%2 == 1:
        return r_list[len(r_list)//2]
    return (r_list[(len(r_list)//2)-1] + r_list[len(r_list)//2])/2

def roll_histogram(testNum,faceNum):
    r_list = roll_list(testNum,faceNum)
    plt.hist(r_list, bins= range(1,faceNum+2), edgecolor="black", linewidth=1, alpha=0.85)
    plt.xticks(range(1, faceNum+1))
    plt.show()

def higherThan(r_list,toBeat):
    r_list = sorted(r_list)
    lo = 0
    hi = len(r_list)
    while lo<hi:
        mid = (lo + hi)//2
        if r_list[mid] <= toBeat:
            lo = mid + 1
        else:
            hi = mid
    return len(r_list) - lo

