<<<<<<< HEAD
def gcd(a,b):
    if a==b:
        return (0,0)
    else:
        x=abs(a-b)

        c=a%x
       
        v=min(c,x-c)
        return(x,v)
    

n=int(input())
result=[]
for _ in range(n):
    a,b=map(int,input().split())
    result.append(gcd(a,b))

for res in result:
    print(*res) 


=======
def gcd(a,b):
    if a==b:
        return (0,0)
    else:
        x=abs(a-b)

        c=a%x
       
        v=min(c,x-c)
        return(x,v)
    

n=int(input())
result=[]
for _ in range(n):
    a,b=map(int,input().split())
    result.append(gcd(a,b))

for res in result:
    print(*res) 


>>>>>>> 08eb3809febe6da35a2f53c953138d330244a0ba
