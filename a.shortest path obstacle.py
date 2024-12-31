n=int(input())

for i in range(n):
    x1,y1=map(int,input().split())
    x2,y2=map(int,input().split())
    f1,f2=map(int,input().split())

    if (x1==x2==f1 and min(y2,y1)<f2<max(y1,y2)) or (y1==y2==f2 and min(x2,x1)<f1<max(x1,x2)):
        print(abs(x1-x2)+abs(y1-y2)+2)
    else:
        print(abs(x1-x2)+abs(y1-y2))
    
