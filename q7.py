num=int(input('Digite o primeiro número: '))
num2=int(input('Digite o segundo número: '))
if num%2==0 and num2%2==0:
    print(num+num2)
else:
    print(num-num2)
if num%2==0 and num2%2==1:
    print(num*num2)