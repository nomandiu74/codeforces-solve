k=int(input())
a=list(map(int,input().split()))
a.sort(reverse=True)
x=0
z=0
if k==0:
    print(0)
else:
    for i in range(len(a)):
        z+=a[i]
        x+=1
        if z>=k:
            print(x)
            break
    
if z<k:
    print(-1)
    
