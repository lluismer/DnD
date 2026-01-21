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
    dice: Dice
    dmg_modifier: int
    dmg_type: DamageType

@dataclass
class ToHit:
    hit_mod: int
    bonus_dice: List[Dice]

@dataclass
class Attack:
    to_hit: ToHit
    damage: List[Damage]

@dataclass
class Defender:
    ac: int
    resistance: Set[DamageType]
    immunity: Set[DamageType]

@dataclass
class AttackTry:
    roll: int
    rollAfterMod: int
    dmg: int
    crit: bool
    hit: bool