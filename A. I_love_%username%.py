<<<<<<< HEAD
def solve():
    n =int(input())
    l =list(map(int,input().split()))

    s = 0


    max_score=l[0]
    min_score=l[0]
    for i in range(1, n):
        if l[i]>max_score:
            s+=1
            max_score=l[i]
        elif l[i]<min_score:
            s+=1
            min_score=l[i]
    print(s)

solve()
=======
def solve():
    n =int(input())
    l =list(map(int,input().split()))

    s = 0


    max_score=l[0]
    min_score=l[0]
    for i in range(1, n):
        if l[i]>max_score:
            s+=1
            max_score=l[i]
        elif l[i]<min_score:
            s+=1
            min_score=l[i]
    print(s)

solve()
>>>>>>> 08eb3809febe6da35a2f53c953138d330244a0ba
