from classes import Attack, Defender, DamageType, Dice, Damage, ToHit
from dice_roll import dice_roll,d20

def dmg(attack: Attack,defender: Defender,crits: int):
    dmg_global = 0
    dmg_attack = 0
    for i in attack.damage:
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

def avgDmgXturn(attack: Attack,defender: Defender,try_num: int = 100000):
    is_crit = 0
    hits = 0
    results = []


    for i in range(try_num):
        bonus_dice_rolls = []
        for j in attack.to_hit.bonus_dice:
            for s in range(j.number):
                bonus_dice_rolls.append(dice_roll(j.faces))
        roll = d20()
        roll_afterMod = roll + attack.to_hit.hit_mod + sum(bonus_dice_rolls)
        is_crit = (roll == 20)
        if roll_afterMod >= defender.ac or is_crit == True:
            hits = 1
        else:
            hits = 0
            results.append((roll_afterMod,0))
        
        if hits == 1 and roll != 1:
            dmg = dmg(attack,defender,is_crit)
            results.append((roll_afterMod,dmg))
    return results