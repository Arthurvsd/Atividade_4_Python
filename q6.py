idade=0
nome=''
cont=1
while cont==1:
    novaidade=int(input('Qual a idade da pessoa? '))
    novonome=str(input('Qual o nome da pessoa? '))
    if novaidade%2==0:
        if novaidade>idade:
            nome=novonome
            idade=novaidade
    else:
        print('A idade não é par')
    cont=int(input('Quer adicionar outra pessoa?Digite 1 para: sim e 2 para: não.'))
print('O nome da pessoa mais velha é: ',nome)
    