n=int(input())
l=[]
for _ in range(n):
    x=int(input())
    v=input()

    if len(v)==1:
        l.append("YES")
    elif v.count('0')==1 and v.count('1')==1:
        l.append("YES")
    else:
        l.append("NO")
print(*l,sep='\n')