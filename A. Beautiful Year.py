x=int(input())
for i in range(1000):
    x+=1
    f=set(str(x))

    if 4==len(f):
        print(x)
        break
