from classes import Attack, Defender, DamageType, Dice, Damage, ToHit, AttackTry, TurnTry, Character
from dice_roll import dice_roll,d20
from modules.test.Characters import fyn
from modules.test.Monster import earth_elemental
import random



def dmg(attack: Attack, defender: Character,crits: bool):
    dmg_global = 0
    for i in attack.damage:
        dmg_attack = 0
        dmg_attack += i.dmg_modifier
        for j in range(i.dice.number):
            dmg_attack += dice_roll(i.dice.faces)
        if crits == True:
            dmg_attack += i.dice.faces * i.dice.number
        if i.dmg_type in defender.defense.resistance:
            dmg_attack = dmg_attack//2
        if i.dmg_type in defender.defense.immunity:
            dmg_attack = 0
        dmg_global += dmg_attack
    return dmg_global

def attackTurnMonster(attacker: Character, defender: Character):
        bonus_dice_rolls = []
        dmgs = 0
        is_crit = False
        hits = False
        attack = random.choice(attacker.attack_list)

        for j in attack.to_hit.bonus_dice:
            for s in range(j.number):
                bonus_dice_rolls.append(dice_roll(j.faces))

        roll = d20()
        roll_afterMod = roll + attack.to_hit.hit_mod + sum(bonus_dice_rolls)
        is_crit = (roll == 20)

        if roll_afterMod >= defender.defense.ac and roll != 1 or is_crit:
            hits = True
        else:
            hits = False
            return AttackTry(roll,roll_afterMod,dmgs,is_crit,hits,defender.defense.ac,attack.name)
        
        if hits and roll != 1:
            dmgs = dmg(attack,defender,is_crit)
            defender.takeDamage(dmgs)
            return AttackTry(roll,roll_afterMod,dmgs,is_crit,hits,defender.defense.ac,attack.name)