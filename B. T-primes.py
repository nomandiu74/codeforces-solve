import sys
import math
LIMIT=int(10**6)
is_prime=[True]*(LIMIT+1)
is_prime[0]=is_prime[1]=False

for i in range(2,int(math.sqrt(LIMIT))+1):
    if is_prime[i]:
        for j in range(i*i,LIMIT+1,i):
            is_prime[j]=False
t_prime_set=set()
for i in range(2,LIMIT+1):
    if is_prime[i]:
        t_prime_set.add(i*i)
n=int(input())
a=list(map(int,input().split()))

for num in a:
    if num in t_prime_set:
        print("YES")
    else:
        print("NO")