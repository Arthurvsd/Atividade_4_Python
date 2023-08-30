num=2
vsoma=0
cont=0

for i in range(50):
    if cont==0:
        vsoma+=num
        cont+=1
    else:
        vsoma-=num
        cont=0
    num+=2
print('A soma dos númeors dá: ',vsoma)