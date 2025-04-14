t=int(input())
for _ in range(t):
    a,b,c,p=map(int,input().split())
    result=a+b+c+p
    if result%3!=0:
        print("NO")
    else:
        max_coin=max(a,b,c)
        coin_need=3*max_coin-(a+b+c)

        if p>=coin_need:
            print("YES")
        else:
            print("NO")