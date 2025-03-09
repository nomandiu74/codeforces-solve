import math
n,h=map(int,input().split())
s=list(map(int,input().split()))
add=0
for f in s:
    if f>h:
        add+=math.ceil(f/h)
    else:
        add+=1
print(add)
