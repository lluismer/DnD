from classes import *

fyn = Character(
    name = "Fyn",
    hp = 38,
    defense = Defender(
        ac = 16,  # Armor Class 16
        resistance = {DamageType.POISON},
        immunity = set(),
    ),
    attack_list=[
        Attack(
            name = "Longbow (Repeating Shot)",
            attacks_per_action = 2,  
            to_hit = ToHit(8, []),   
            damage = [Damage(Dice(1, 8), 5, DamageType.PIERCING)],  
        ),
        Attack(
            name="Fire Bolt",
            attacks_per_action=1,
            to_hit=ToHit(7, []),  
            damage=[Damage(Dice(2, 10), 0, DamageType.FIRE)],  
        ),
        Attack(
            name="Unarmed Strike",
            attacks_per_action=1,
            to_hit=ToHit(5, []), 
            damage=[Damage(Dice(0, 1), 3, DamageType.BLUDGEONING)],
        ),
    ],
)
