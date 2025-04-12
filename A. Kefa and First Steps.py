n=int(input())
a=list(map(int,input().split()))
x=1
max_len=1

for i in range(n-1):
    if a[i]<=a[i+1]:
        x+=1
        max_len=max(max_len,x)
    else:
        x=1
print(max_len)
