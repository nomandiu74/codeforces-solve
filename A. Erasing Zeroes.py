<<<<<<< HEAD
n=int(input())
q=[]
for i in range(n):
    x=input()

    l=x.find('1')
    z=x.rfind('1')
    new=x[l:z+1]
    ans=new.count('0')
    q.append(ans)

print(*q,sep="\n")
=======
n=int(input())
q=[]
for i in range(n):
    x=input()

    l=x.find('1')
    z=x.rfind('1')
    new=x[l:z+1]
    ans=new.count('0')
    q.append(ans)

print(*q,sep="\n")
>>>>>>> 08eb3809febe6da35a2f53c953138d330244a0ba
