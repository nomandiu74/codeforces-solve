n,l=map(int,input().split())
a=list(map(int,input().split()))
a.sort()

if n==1:
    result=max(a[0]-0,l-a[0])
else:

    x=[]
    for i in range(n-1):
        x.append(a[i+1]-a[i])
    maximum=(max(x))/2
    front=a[0]-0
    back=l-a[-1]
    result=max(front,back,maximum)
print("{:.10f}".format(result))