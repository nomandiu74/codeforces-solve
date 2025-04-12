n=int(input())
x=0
y=0
for _ in range(n):
    name=input()
    if name=='A':
        x+=1
    else:
        y+=1
if x>y:
    print('A')
else:
    print('ABC')