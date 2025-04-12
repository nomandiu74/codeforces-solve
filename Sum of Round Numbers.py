t=int(input())
for _ in range(t):
    n=int(input())
    r=[]
    x=1
    while n>0:
        if n%10>0:
            r.append(int((n%10))*x)
        n//=10
        x*=10
    print(len(r))
    print(" ".join(map(str,r)))