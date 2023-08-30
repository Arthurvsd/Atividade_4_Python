import random

cont=0
melodia1=random.randint(1,5)
melodia2=random.randint(1,5)
melodia3=random.randint(1,5)
print('As melodias do flautista são:',melodia1,melodia2,melodia3)
tentativa1=random.randint(1,5)
tentativa2=random.randint(1,5)
tentativa3=random.randint(1,5)
print('As tentativas foram:',tentativa1,tentativa2,tentativa3)
while melodia1!=tentativa1 or melodia2!=tentativa2 or melodia3!=tentativa3:
    tentativa1=random.randint(1,5)
    tentativa2=random.randint(1,5)
    tentativa3=random.randint(1,5) 
    cont+=1
print('O número de tentativas foi de:',cont)
print(tentativa1, tentativa2, tentativa3)