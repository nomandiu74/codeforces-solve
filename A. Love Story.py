s='codeforces'
t=int(input())
for _ in range(t):
    a=0
    n=input()
    l=len(n)
    for i in range(l):
        if s[i]!=n[i]:
            a+=1
    print(a)