t=int(input())
mishka=0
cherish=0
for _ in range(t):
    n,m=map(int,input().split())
    if n>m:
        mishka+=1
    elif m==n:
        cherish+=0
        mishka+=0
    else:
        cherish+=1
if mishka>cherish:
    print("Mishka")
elif mishka==cherish:
    print("Friendship is magic!^^")
else:
    print("Chris")
    