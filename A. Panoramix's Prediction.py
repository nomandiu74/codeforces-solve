n,m=map(int,input().split())
l=[]
for i in range(2,m+1):
    prime=True
    for j in range(2,int(i*.5)+1):
        if i%j==0:
            prime=False
            break
    if prime:
        l.append(i)
            


if n not in l or m not in l:
    print("NO")
else:
    for i in range(len(l)-1):
        if l[i]==n and l[i+1]==m:
            print("YES")
            break
        
    else:
        print("NO")  