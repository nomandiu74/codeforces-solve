n,m=map(int,input().split())
is_colored=False
for i in range(n):
 
    x=input().split()

    for pixel in x:
        if pixel in['C','M','Y']:
            is_colored=True
            break
    
if is_colored:
    print("#Color")
else:
    print("#Black&White")