t=int(input())
l=[]
for _ in range(t):
    n,k=map(int,input().split())
    x=list(map(int,input().split()))
    if k>=2:
        l.append("YES")
    elif k==1:
        if x==sorted((x)):
            l.append("YES")
        else:
            l.append("NO")
print(*l,sep='\n')