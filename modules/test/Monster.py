from classes import DamageType,Defender, Character

# Earth Elemental (MM / D&D Beyond)
earth_elemental = Character(
    name="Earth Elemental",
    hp=126,  # 126 (12d10+60)
    defense=Defender(
        ac=17,
        resistance={DamageType.BLUDGEONING, DamageType.PIERCING, DamageType.SLASHING},
        immunity={DamageType.POISON},
    ),
    attack_list=[
        Attack(
            name="Slam",
            attacks_per_action=2,  # Multiattack: two slam attacks
            to_hit=ToHit(hit_mod=8, bonus_dice=[]),  # +8 to hit
            damage=[Damage(Dice(2, 8), 5, DamageType.BLUDGEONING)],  # 2d8+5 bludgeoning
        )
    ],
)
