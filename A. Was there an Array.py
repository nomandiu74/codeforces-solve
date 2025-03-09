t=int(input())

for _ in range(t):
    n=int(input())
    x=list(map(int,input().split()))
    s=0
    for i in range(1,len(x)-1):
        if x[i-1]==1 and x[i]==0 and x[i+1]==1:
            s=1
            break
    if s==0:
        print("YES")
    else:
        print("NO")
        
    
        