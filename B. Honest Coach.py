t=int(input())
for _ in range(t):
    n=int(input())
    l=[]
    x=list(map(int,input().split()))
    x.sort()
    for i in range(n-1):
        y=abs(x[i]-x[i+1])
        l.append(y)
    print(min(l))