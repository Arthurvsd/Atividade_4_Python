s=0
for n in range(1,51):
    if s==0 or s==1:
        print('+',n)
        s=s+1
    if s==2 or s==3:
        print('-',n)
        s=s+1
    if s==4:
        print('+',n)
        s=s+1
    if s==5:
        print('-',n)
        s=0
print(n)
    