t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    if sum(arr)%2==1:
        print("YES")
    elif all(x%2==0 for x in arr):
        print("NO")
    elif all(x%2==1 for x in arr) and sum(arr)%2==0:
        print("NO") 
    else:
        print("YES")