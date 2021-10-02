t=int(input())
for i in range(t):
    n=int(input())
    c=n%4
    k=n//4
    if k>=1:
        if c==0:
            a=((k-1)*44)+60
        elif c==1:
            a=((k)*44)+32
        elif c==2:
            a=((k)*44)+44
        elif c==3:
            a=((k)*44)+55
    else:
        if c==0:
            a=0
        elif c==1:
            a=20
        elif c==2:
            a=36
        elif c==3:
            a=51
    print(a)
