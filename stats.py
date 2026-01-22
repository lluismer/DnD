from classes import Attack, Defender, DamageType, Dice, Damage, ToHit, AttackTry, TurnTry
from dice_roll import dice_roll,d20
import matplotlib.pyplot as plt
from modules.test.attacks import firebolt, longbow_2, longbow_brandingSmite
from modules.test.defenders import earth_elemental, orc
import matplotlib

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

def attackTurn(attack: Attack, defender: Defender):
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
            return AttackTry(roll,roll_afterMod,dmgs,is_crit,hits,defender.ac,attack.name)
        
        if hits and roll != 1:
            dmgs = dmg(attack,defender,is_crit)
            return AttackTry(roll,roll_afterMod,dmgs,is_crit,hits,defender.ac,attack.name)

def avgDmgXturn(attack: Attack,defender: Defender,try_num: int = 100000):
    results = []


    for i in range(try_num):
        turn_dmg = 0
        turn_hits = 0

        for _ in range(attack.attacks_per_action):
            tr = attackTurn(attack,defender)
            if tr.dmg >= 0:
                turn_dmg += tr.dmg
            if tr.hit:
                turn_hits += 1
        results.append(TurnTry(turn_dmg,turn_hits,attack.name))



    return results

def plotHistDmg(results: list):
    y_dmg  = []
    name = results[0].name
    for i in results:
        y_dmg.append(i.dmg)
    avg = average(y_dmg)
    med = median(y_dmg)
    plt.hist(y_dmg, bins=30, edgecolor="black", alpha=0.8)
    plt.axvline(med, color="red", linestyle="--", linewidth=2, label=f"Median = {med}")
    plt.axvline(avg, color="blue", linestyle="--", linewidth=2, label=f"Average = {avg}")
    plt.xlabel(f"Damage by {name}")
    plt.ylabel("Count")
    plt.show()

def plotBoxDmg(results: list):
    y_dmg = []
    name = results[0].name
    for i in results:
        y_dmg.append(i.dmg)
    plt.figure()
    plt.boxplot([y_dmg], tick_labels=[name], showfliers=False)
    plt.ylabel("Damage per turn")
    plt.title(f"{name}: damage boxplot")
    plt.show()

def plt2BoxDmg(result1,result2):
    y_dmg1 = []
    y_dmg2 = []
    name1 = result1[0].name
    name2 = result2[0].name
    for i in result1:
        y_dmg1.append(i.dmg)
    for i in result2:
        y_dmg2.append(i.dmg)
    plt.figure()
    plt.boxplot([y_dmg1,y_dmg2], tick_labels=[name1,name2], showfliers=True)
    plt.ylabel("Damage per turn")
    plt.title("Damage boxplot")
    plt.show()

def plt3BoxDmg(result1,result2,result3):
    y_dmg1 = []
    y_dmg2 = []
    y_dmg3 = []
    name1 = result1[0].name
    name2 = result2[0].name
    name3 = result3[0].name
    for i in result1:
        y_dmg1.append(i.dmg)
    for i in result2:
        y_dmg2.append(i.dmg)
    for i in result3:
        y_dmg3.append(i.dmg)
    plt.figure()
    plt.boxplot([y_dmg1,y_dmg2,y_dmg3], tick_labels=[name1,name2,name3], showfliers=True)
    plt.ylabel("Damage per turn")
    plt.title("Damage boxplot")
    plt.show()

def plotBoxDmgOnHit(results: list):
    y_dmg = []
    name = results[0].name
    for i in results:
        if i.dmg > 0:
            y_dmg.append(i.dmg)
    plt.figure()
    plt.boxplot([y_dmg], tick_labels=[name], showfliers=False)
    plt.ylabel("Damage per turn")
    plt.title(f"{name}: damage boxplot")
    plt.show()

def plt2BoxDmgOnHit(result1,result2):
    y_dmg1 = []
    y_dmg2 = []
    name1 = result1[0].name
    name2 = result2[0].name
    for i in result1:
        if i.dmg > 0:
            y_dmg1.append(i.dmg)
    for i in result2:
        if i.dmg > 0:
            y_dmg2.append(i.dmg)
    plt.figure()
    plt.boxplot([y_dmg1,y_dmg2], tick_labels=[name1,name2], showfliers=True)
    plt.ylabel("Damage per turn")
    plt.title("Damage boxplot")
    plt.show()

def plt3BoxDmgOnHit(result1,result2,result3):
    y_dmg1 = []
    y_dmg2 = []
    y_dmg3 = []
    name1 = result1[0].name
    name2 = result2[0].name
    name3 = result3[0].name
    for i in result1:
        if i.dmg > 0:
            y_dmg1.append(i.dmg)
    for i in result2:
        if i.dmg > 0:  
            y_dmg2.append(i.dmg)
    for i in result3:
        if i.dmg > 0:
            y_dmg3.append(i.dmg)
    plt.figure()
    plt.boxplot([y_dmg1,y_dmg2,y_dmg3], tick_labels=[name1,name2,name3], showfliers=True)
    plt.ylabel("Damage per turn")
    plt.title("Damage boxplot")
    plt.show()


firebolt_avg = avgDmgXturn(firebolt,orc)
longbow_2_avg = avgDmgXturn(longbow_2,orc)
longbow_brand_avg = avgDmgXturn(longbow_brandingSmite,orc)
#plotHistDmg(avgDmgXturn(firebolt,earth_elemental))
#plotBoxDmg(avgDmgXturn(firebolt,earth_elemental))
plt3BoxDmgOnHit(firebolt_avg,longbow_brand_avg,longbow_2_avg)