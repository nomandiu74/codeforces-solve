import math
n,k=map(int,input().split())
members=list(map(int,input().split()))
x=[]
for i in range(len(members)):
    if 5-members[i]>=k:
        x.append(members[i])

result=math.floor(len(x)/3)
print(result)