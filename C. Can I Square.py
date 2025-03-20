import math
t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    x=sum(l)

    sqrt_x=math.isqrt(x)
    if sqrt_x*sqrt_x==x:
        print("YES")
    else:
        print("NO")
   