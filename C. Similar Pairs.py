t=int(input())
for _ in range(t):
    n=int(input())
    x=list(map(int, input().split()))
    odd = 0
    for i in x:
        if i%2==1:
            odd+=1
    if odd%2==0:
        print("YES")
    else:
        x.sort()
        pair=0
        for i in range(n - 1):
            if abs(x[i] - x[i + 1]) == 1:
                pair=1
                break
        if pair==1:
            print("YES")
        else:
            print("NO")