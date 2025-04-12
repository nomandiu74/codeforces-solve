t=int(input())
for _ in range(t):
    n=int(input())
    x=list(map(int,input().split()))
    mihai=0
    bisha=0
    for i in range(n):
        if x[i]%2==0:
            mihai+=x[i]
        else:
            bisha+=x[i]
    if mihai>bisha:
        print("YES")
    else:
        print("NO")