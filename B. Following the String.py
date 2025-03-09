t=int(input())
letter="abcdefghijklmnopqrstuvwxyz"
while t>0:
    t-=1

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


