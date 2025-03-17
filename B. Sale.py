n,m=map(int,input().split())
l=list(map(int,input().split()))
l.sort()
z=l[:m]
x=0

for i in range(len(z)):
    if z[i]<=0:
        x+=z[i]
print(-x)