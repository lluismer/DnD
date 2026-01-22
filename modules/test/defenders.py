from classes import DamageType,Defender

earth_elemental = Defender(17,{DamageType.BLUDGEONING, DamageType.PIERCING, DamageType.SLASHING},
    {DamageType.POISON})

orc = Defender(13,{},{})