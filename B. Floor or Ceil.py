import math
t=int(input())
for _ in range(t):
    x,n,m=map(int,input().split())
    if n>x and m>x:
        print(0,0)
    else:
        min_x=x
        for _ in range(n):
            min_x//=2
            if min_x==0:
                break
        for _ in range(m):
            min_x=(min_x + 1) // 2
            if min_x==0:
                break
        max_x=x
        for _ in range(m):
            max_x=(max_x + 1)//2
        for _ in range(n):
            max_x//=2
        print(max_x,min_x)