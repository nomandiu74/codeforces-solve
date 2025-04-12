n=int(input())
laptop=[]
for _ in range(n):
    p,q=map(int,input().split())
    laptop.append((p,q))
laptop.sort()
max_far=0
alex_happy=0
for _,q in laptop:
    if q<max_far:
        alex_happy=1
        break
    max_far=max(max_far,q)

if alex_happy==1:
    print("Happy Alex")
else:
    print("Poor Alex")
