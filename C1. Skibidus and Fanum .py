t=int(input())

for _ in range(t):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))

    l=[]

    if n==m:
        print("YES")
    else:
        for i in range(n):
            mnimum=min(a[i],b[0]-a[i])
            if i>0 and l[i-1]>mnimum:
                l.append(max(a[i],b[0]-a[i]))
            else:
                l.append(mnimum)
       #print(l)


##############Non-decreasing order check#############
        s=0

        for i in range(len(l)-1):
            if l[i]<=l[i+1]:
                s=1
            else:
                s=0
                break
        if s==0:
            print("NO")
        else:
            print("YES")
