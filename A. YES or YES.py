<<<<<<< HEAD
n=int(input())
l=[]
for _ in range(n):
    x=input()
    s=0
    if len(x)>=3:
        if x[0]== 'Y' or x[0]=='y':
            s+=1
        if x[1]== 'E' or x[1]=='e':
            s+=1
        if x[2]== 'S' or x[2]=='s':
            s+=1
    if s==3:
        l.append("YES")
    else:
        l.append("NO")
        
print(*l,sep='\n')


=======
n=int(input())
l=[]
for _ in range(n):
    x=input()
    s=0
    if len(x)>=3:
        if x[0]== 'Y' or x[0]=='y':
            s+=1
        if x[1]== 'E' or x[1]=='e':
            s+=1
        if x[2]== 'S' or x[2]=='s':
            s+=1
    if s==3:
        l.append("YES")
    else:
        l.append("NO")
        
print(*l,sep='\n')


>>>>>>> 08eb3809febe6da35a2f53c953138d330244a0ba
