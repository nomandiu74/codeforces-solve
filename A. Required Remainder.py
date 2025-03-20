t=int(input())
for _ in range(t):
    i,j,k=map(int,input().split())
    n=(k-j)//i
    x=n*i+j
    print(x)