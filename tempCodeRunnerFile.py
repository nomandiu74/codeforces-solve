<<<<<<< HEAD
t=int(input())
letter="abcdefghijklmnopqrstuvwxyz"
for _ in range(t):

    n=int(input())

    dictionary={}
    for ch in letter:
        dictionary[ch]=0
    

    v=list(map(int,input().split()))

    for i in range(n):
        for ch in letter:
            if dictionary[ch]==v[i]:
                print(ch,end="")
                dictionary[ch]+=1
                break
    print()

    
=======
a,b=map(int,input().split())

for i in range(a):
    if i%2==0:
        print("#"*b)
    else:
        if i%4==1:
            print("."*(b-1)+"#")
        else:
            print("#"+"."*(b-1))
>>>>>>> 08eb3809febe6da35a2f53c953138d330244a0ba
