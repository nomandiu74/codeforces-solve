t=int(input())
s='aeiou'
for _ in  range(t):
    n=int(input())
    x=(s*((n//len(s)+1)))[:n]
    
    z=sorted(x)
    print(''.join(z))