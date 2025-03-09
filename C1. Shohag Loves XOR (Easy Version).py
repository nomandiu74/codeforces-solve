<<<<<<< HEAD
def bitopr(x,m):
    count=0
    l=min(2*x,m)

    for y in range(1,l+1):
        if x!=y:
            xor=x^y
            if x%xor==0 or y%xor==0:
                count+=1
    return count


n=int(input()) 
for _ in range(n):
    x,m=map(int,input().split())
    result=bitopr(x,m)
    print(result)


=======
def bitopr(x,m):
    count=0
    l=min(2*x,m)

    for y in range(1,l+1):
        if x!=y:
            xor=x^y
            if x%xor==0 or y%xor==0:
                count+=1
    return count


n=int(input()) 
for _ in range(n):
    x,m=map(int,input().split())
    result=bitopr(x,m)
    print(result)


>>>>>>> 08eb3809febe6da35a2f53c953138d330244a0ba
