from dataclasses import dataclass, field
from typing import List, Set
from enum import IntEnum

class DamageType(IntEnum):
    BLUDGEONING = 0
    PIERCING = 1
    SLASHING = 2
    FIRE = 3
    COLD = 4
    LIGHTNING = 5
    ACID = 6
    POISON = 7
    PSYCHIC = 8
    NECROTIC = 9
    RADIANT = 10
    THUNDER = 11
    FORCE = 12

@dataclass
class Dice:
    """ Represent dices in NdF format (2d6).

    number: How many dice are rolled (N).
    faces:  How many faces each die has (F).
    """
    number: int
    faces: int

@dataclass
class Damage:
    """ Represent the damage dice and type
    
    dice:         A dice Dataclass
    dmg_modifier: The bonus to the attack if it hits
    dmg_type:     The damage type
    """
    dice: Dice
    dmg_modifier: int
    dmg_type: DamageType

@dataclass
class ToHit:
    """ Represent the modifier to a d20 hit dice

    hit_mod:        Flat bonus to the d20 roll
    bonus_dice:     List of bonuses dices to the d20 roll
    """
    hit_mod: int
    bonus_dice: List[Dice]

@dataclass
class Attack:
    """ Represent all the logic behind an attack

    to_hit:             Bonuses to d20 hit dice
    damage:             Damage roll, bonuses and type
    name:               Name of the attack
    attacks_per_action: Number of attacks you can do per turn
    """
    to_hit: ToHit
    damage: List[Damage]
    name: str
    attacks_per_action: int

@dataclass
class Defender:
    """ Represent a character defenses against attacks

    ac:         The armor class of the character
    resistance: The list of resistances of the character
    immunity:   The list of immunities of the character
    """
    ac: int
    resistance: List[DamageType]
    immunity: List[DamageType]

@dataclass
class AttackTry:
    """ Represent a single attack action

    roll:           The base roll of the attack
    rollAfterMod:   The roll after all the modifiers
    dmg:            The dmg of the attack
    crit:           If True is a critical attack, if False not critical
    hit:            If True the attack hitted, else didn't hit
    ac:             Armor class of the defender
    name:           Name of the attack used
    """
    roll: int
    rollAfterMod: int
    dmg: int
    crit: bool
    hit: bool
    ac: int
    name: str

@dataclass
class TurnTry:
    """ Represent a turn

    dmg:    The total damage of the turn
    hits:   How many attacks hitted in the turn
    name:   Name of the attack used in the turn
    """
    dmg: int
    hits: int
    name: List[str]

@dataclass
class Character:
    """ Represent a game character or monster

    attack_list: List of Attacks that the character has
    defense:     The character defensive variables
    name:        Name of the character
    hp:          Hit points of the Character
    """
    attack_list: list[Attack]
    defense: Defender
    name: str
    hp: int
    
    def takeDamage(self,amount: int):
        self.hp = max(0,self.hp - amount)
    
    def isDead(self):
        return (self.hp == 0)