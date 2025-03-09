<<<<<<< HEAD
t=int(input())


for _ in range(t):
    n=int(input())
    s=input()

    ans=0

    for i in range(1,n):
        if s[i]=='@':
            ans+=1
        if s[i]=='*' and s[i-1]=='*':
            break
 
=======
t=int(input())


for _ in range(t):
    n=int(input())
    s=input()

    ans=0

    for i in range(1,n):
        if s[i]=='@':
            ans+=1
        if s[i]=='*' and s[i-1]=='*':
            break
 
>>>>>>> 08eb3809febe6da35a2f53c953138d330244a0ba
    print(ans)