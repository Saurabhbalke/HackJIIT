t=int(input())
for i in range(t):
    n,k=map(int,input().split( ))
    s=input()[:n]
    a='*'
    c=0
    res=[]
    for ele in s:
        if ele==a:
            c+=1
        else:
            res.append(c)
            c=0
    if s[-1]=="*":
        res.append(c)
    if k<=max(res):
        print("YES")
    else:
        print("NO")
