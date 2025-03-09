<<<<<<< HEAD
t=int(input())
s='aeiou'
for _ in  range(t):
    n=int(input())
    x=(s*((n//len(s)+1)))[:n]
    
    z=sorted(x)
=======
t=int(input())
s='aeiou'
for _ in  range(t):
    n=int(input())
    x=(s*((n//len(s)+1)))[:n]
    
    z=sorted(x)
>>>>>>> 08eb3809febe6da35a2f53c953138d330244a0ba
    print(''.join(z))