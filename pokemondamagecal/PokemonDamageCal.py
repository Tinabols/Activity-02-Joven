import random
from time import sleep

Level = 90
A = 205
D = 188
Power = 110


Targets = 1
Weather = 1
Badge = 1
Critical = 1
Random1 = random.uniform(0.85,1.00)
STAB = 1.5
Type = 0.5
Burn = 1


Modifier =(Targets*Weather*Badge*Critical*Random1*STAB*Type*Burn*1)
Damage = ((((((2*Level/5)+2)*Power)*(A/D)))/(50+2)*Modifier)


print("A Lv.90 Charizard is against a Lv.95 Feraligatr")
sleep(3.00)
print("Charizard used Fire Blast!")
sleep(3.00)
print("It's not very effective...")
sleep(3.00)
print("Charizard's attack dealt only",round(Damage),"damage to Feraligatr")
