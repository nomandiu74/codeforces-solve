t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    T=s.count("T")
    i=s.count("i")
    m=s.count("m")
    u=s.count("u")
    r=s.count("r")
    
    if n==5 and T==1 and i==1 and m==1 and u==1 and r==1:
        print("YES")
    else:
        print("NO")