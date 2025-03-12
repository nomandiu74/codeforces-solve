t=int(input())

for _ in range(t):
    n=int(input())
    a=list(map(int, input().split()))

    odd=0
    even=0
    for i in range(n):
        if i%2==0 and a[i]%2!=0:
            even+=1
        elif i%2==1 and a[i]%2!=1:
            odd+=1
    if odd!=even:
        print(-1)
    else:
        print(odd)
