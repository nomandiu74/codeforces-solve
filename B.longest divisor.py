<<<<<<< HEAD
t=int(input())
for _ in range(t):
    x=int(input())
    z=[]
    for i in range(1,100):
        z.append(x%i)
    
    s=0
    for j in range(len(z)):
        if z[j]==0:
            s+=1
        else:
            break
    print(s)
        
=======
t=int(input())
for _ in range(t):
    x=int(input())
    z=[]
    for i in range(1,100):
        z.append(x%i)
    
    s=0
    for j in range(len(z)):
        if z[j]==0:
            s+=1
        else:
            break
    print(s)
        
>>>>>>> 08eb3809febe6da35a2f53c953138d330244a0ba
    