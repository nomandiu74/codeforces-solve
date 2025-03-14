from math import gcd
yak,wak=map(int,input().split())
maximum=max(yak,wak)
d=6-maximum+1
y=6
x=gcd(y,d)
d//=x
y//=x
print("{}/{}".format(d,y))