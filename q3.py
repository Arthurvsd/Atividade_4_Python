import random
contador=0
pedireito=0
peesquerdo=0
for contador in range(1, 151):
    pe=random.randint(1,2)
    if pe==1:
        pedireito=pedireito+1
        contador=contador+1
    else:
        peesquerdo=peesquerdo+1
        contador=contador+1
print('Ligeirinho pegou:',pedireito,'queijos.')