t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    j=list(map(int,input().split()))
    i=list(map(int,input().split()))
    i.sort(reverse=True)
    j.sort()
    for x in range(min(k,len(j),len(i))):
        if i[x]>j[x]:
            j[x],i[x]=i[x],j[x]
        else:
            break

    print(sum(j))
    
