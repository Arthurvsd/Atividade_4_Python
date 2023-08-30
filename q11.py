import random
lucro = 0
cont=0
moto=0
carro=0
onibus=0
for veiculo in range(1,401):
    opcao = random.randint(1,3)
    if opcao == 1:
        lucro = lucro + 4
        moto=moto+1
    elif opcao == 2:
        lucro = lucro + 8
        carro=carro+1
    elif opcao == 3:
        lucro = lucro + 20
        onibus=onibus+1
print('Moto:',moto,'\nCarro:',carro,'\nOnibus:',onibus)
print('O lucro do estacionamento foi R$',lucro)     