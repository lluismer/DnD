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


longbow = Attack(
            name = "Longbow (Repeating Shot)",
            attacks_per_action = 2,  
            to_hit = ToHit(8, []),   
            damage = [Damage(Dice(1, 8), 5, DamageType.PIERCING)],  
        )
fireball = Attack(
            name="Fire Bolt",
            attacks_per_action=1,
            to_hit=ToHit(7, []),  
            damage=[Damage(Dice(2, 10), 0, DamageType.FIRE)],  
        )
longbow_branding = Attack(
            name = "Longbow (Repeating Shot)",
            attacks_per_action = 2,  
            to_hit = ToHit(8, []),   
            damage = [Damage(Dice(1, 8), 5, DamageType.PIERCING),Damage(Dice(2,6),0,DamageType.RADIANT)],  
        )

windvane = Attack(
            name = "Windvane",
            attacks_per_action = 2,  
            to_hit = ToHit(9, []),   
            damage = [Damage(Dice(1, 6), 6, DamageType.PIERCING),Damage(Dice(1,6),0,DamageType.LIGHTNING)],  
        )

windvane_meelee = Attack(
            name = "Windvane_meele",
            attacks_per_action = 2,  
            to_hit = ToHit(9, []),   
            damage = [Damage(Dice(1, 8), 6, DamageType.PIERCING),Damage(Dice(1,6),0,DamageType.LIGHTNING)],  
        )

Eldritch_Smite = Attack(
            name = "Eldritch_Smite",
            attacks_per_action = 1,  
            to_hit = ToHit(9, []),   
            damage = [Damage(Dice(1, 8), 6, DamageType.PIERCING),Damage(Dice(1,6),0,DamageType.LIGHTNING),Damage(Dice(4,8),0,DamageType.FORCE),Damage(Dice(1,8),6,DamageType.PIERCING),Damage(Dice(1,6),0,DamageType.LIGHTNING)],  
        )

