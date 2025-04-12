n=int(input())
l=[]
for _ in range(n):
    name=input()
    l.append(name)
val={}

for tem in l:
    if tem in val:
        val[tem]+=1
    else:
        val[tem]=1
win=(max(val,key=val.get))
print(win)