import random
tiros=0
erros=0
acertos=0
num=random.randint(12, 299)
while tiros<195:
    if num%11==0:
        tiros=tiros+1
        acertos=acertos+1
    else:
        num=random.randint(12, 299)
        tiros=tiros+1
        erros=erros+1
print('Quantidade de países atingidos: ',acertos)
