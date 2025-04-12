t=int(input())
for _ in range(t):
    n=int(input())
    candy=list(map(int,input().split()))
    orange=list(map(int,input().split()))
    min_candy=min(candy)
    min_orange=min(orange)
    result=0
    for i in range(n):
        x=max((candy[i]-min_candy),(orange[i]-min_orange))
        result+=x
    print(result)