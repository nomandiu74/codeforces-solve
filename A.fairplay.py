t=int(input())
for _ in range(t):
    i,j,k,l=map(int,input().split())
    x=max(i,j)
    y=max(k,l)
    w=min(i,j)
    z=min(k,l)
    if z<x and z<y and w<x and w<y:
        print("YES")
    else:
        print("NO")