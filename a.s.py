t=int(input())
results=[]

for _ in range(t):
    n, x=map(int,input().split())
    a=list(map(int, input().split()))
    
    total_sum=sum(a)
    
    if total_sum%n==0 and total_sum//n==x:
        results.append("YES")
    else:
        results.append("NO")
for result in results:
    print(result)
