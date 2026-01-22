from classes import Attack, Defender, DamageType, Dice, Damage, ToHit, AttackTry
from dice_roll import dice_roll,d20
import matplotlib.pyplot as plt
from modules.test.attacks import firebolt
from modules.test.defenders import earth_elemental

def average(r_list: list):
    return sum(r_list)/len(r_list)

def median(r_list: list):
    r_list = sorted(r_list)
    if len(r_list)%2 == 1:
        return r_list[len(r_list)//2]
    return (r_list[(len(r_list)//2)-1] + r_list[len(r_list)//2])/2


def dmg(attack: Attack,defender: Defender,crits: bool):
    dmg_global = 0
    for i in attack.damage:
        dmg_attack = 0
        dmg_attack += i.dmg_modifier
        for j in range(i.dice.number):
            dmg_attack += dice_roll(i.dice.faces)
        if crits == True:
            dmg_attack += i.dice.faces * i.dice.number
        if i.dmg_type in defender.resistance:
            dmg_attack = dmg_attack//2
        if i.dmg_type in defender.immunity:
            dmg_attack = 0
        dmg_global += dmg_attack
    return dmg_global

def avgDmgXturn(attack: Attack,defender: Defender,try_num: int = 1000):
    results = []

    for i in range(try_num):
        bonus_dice_rolls = []
        dmgs = 0
        is_crit = False
        hits = False

        for j in attack.to_hit.bonus_dice:
            for s in range(j.number):
                bonus_dice_rolls.append(dice_roll(j.faces))

        roll = d20()
        roll_afterMod = roll + attack.to_hit.hit_mod + sum(bonus_dice_rolls)
        is_crit = (roll == 20)

        if roll_afterMod >= defender.ac or is_crit:
            hits = True
        else:
            hits = False
            results.append(AttackTry(roll,roll_afterMod,dmgs,is_crit,hits,defender.ac))
        
        if hits and roll != 1:
            dmgs = dmg(attack,defender,is_crit)
            results.append(AttackTry(roll,roll_afterMod,dmgs,is_crit,hits,defender.ac))

    return results

def plottingDmg(results: list):
    x_ac = []
    y_dmg  = []
    for i in results:
        x_ac.append(i.roll)
        y_dmg.append(i.dmg)
    avg = average(y_dmg)
    med = median(y_dmg)
    plt.hist(y_dmg, bins=30, edgecolor="black", alpha=0.8)
    plt.axvline(med, color="red", linestyle="--", linewidth=2, label=f"Median = {med}")
    plt.axvline(avg, color="blue", linestyle="--", linewidth=2, label=f"Median = {med}")
    plt.xlabel("Damage")
    plt.ylabel("Count")
    plt.show()
    plt.boxplot(y_dmg, showfliers=False)
    plt.ylabel("Damage per turn")
    plt.title("Damage distribution by spell")
    plt.show()



plottingACxDmg(avgDmgXturn(firebolt,earth_elemental))