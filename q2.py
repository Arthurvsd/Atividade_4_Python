import random
mn=random.randint(1000, 4000)
gn=random.randint(1000, 4000)
dg=random.randint(1000, 4000)
ee=random.randint(1000, 4000)
duelo=0
while duelo<2:
    if mn>gn:
        print('Mago Negro ganhou!')
        print('O poder do Mago Negro é de:',mn,', e o do Gênio é de:',gn)
        duelo=duelo+1
    else:
        print('O Gênio ganhou!')
        print('O poder do Mago Negro é de:',mn,', e o do Gênio é de:',gn)
        duelo=duelo+1
    if dg>ee:
        print('O dragão ganhou!')
        print('O poder do Dragão é de:',dg,'e o do ser elétrico é de:',ee)
        duelo=duelo+1
    else:
        duelo=duelo+1
        print('O ser elétrico ganhou!')
        print('O poder do Dragão é de:',dg,'e o do ser elétrico é de:',ee)