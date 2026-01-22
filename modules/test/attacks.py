from classes import Attack,ToHit,Damage,Dice,DamageType

firebolt = Attack(ToHit(8,[]),[Damage(Dice(2,10),0,DamageType(3))],"Firebolt",1)
longbow_2 = Attack(ToHit(8,[]),[Damage(Dice(1,8),5,DamageType(1))],'Longbow',2)
longbow_brandingSmite = Attack(ToHit(8,[]),[Damage(Dice(1,8),5,DamageType(1)),Damage(Dice(2,6),0,DamageType(10))],"Longbow Branding Smite",1)