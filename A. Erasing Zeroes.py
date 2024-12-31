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
