t=int(input())
m=list(map(int,input().split()))
even=0
odd=0
for j in m:
    if j%2==0:
        even+=1
    else:
        odd+=1
if even>odd:
    for i in range(len(m)):
        if m[i]%2==1:
            break
    print(i+1)
else:
    for i in range(len(m)):
        if m[i]%2==0:
            break
    print(i+1)
