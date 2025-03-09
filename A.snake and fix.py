<<<<<<< HEAD
a,b=map(int,input().split())

for i in range(1,a+1):
    if i%2==1:
        print("#"*b)
    elif i%4==2:
        print("."*(b-1)+"#")
    elif i%4==0:
=======
a,b=map(int,input().split())

for i in range(1,a+1):
    if i%2==1:
        print("#"*b)
    elif i%4==2:
        print("."*(b-1)+"#")
    elif i%4==0:
>>>>>>> 08eb3809febe6da35a2f53c953138d330244a0ba
        print("#"+(b-1)*".")