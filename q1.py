import random
boneco=0
tumulo=0
morcego=0
cont=0

while cont<45:
    botao=random.randint(1, 3)
    if botao==1:
        boneco=boneco+1
        cont=cont+1
    elif botao==2:
        tumulo=tumulo+1
        cont=cont+1
    elif botao==3:
        morcego=morcego+1
        cont=cont+1
print('A escola gastou:',boneco*350+tumulo*120+morcego*50)