t=int(input())
for _ in range(t):
    n=int(input())
    s=list(map(int,input().split()))
    s.sort()
    x=0
    for i in range(1,n):
        if s[i]<s[i-1]:
            x=1
            break
    if x==0:
        print("YES")
    else:
        print("NO")