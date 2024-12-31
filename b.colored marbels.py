from collections import Counter
import math

n=int(input())
for _ in range(n):
    m=int(input())
    s=list(map(int,input().split()))

    color_cont=Counter(s)

    individual=len(color_cont)

    count=0
    for c in color_cont.values():
        if c==1:
            count+=1
    alice=individual+math.ceil(count/2)-math.floor(count/2)    
    
    print(alice)