t=int(input())
for i in range(t):
    a=list(int(num) for num in input().strip().split( ))[:7]
    c=a.count(1)
    d=a.count(0)
    if c>d:
        print("yes")
    else:
        print("no")
