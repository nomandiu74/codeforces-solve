import math
t=int(input())
for _ in range(t):
    n=int(input())
    s=str(input())
    count_dash=s.count('-')
    count_u_line=s.count('_')

    countd=math.floor(count_dash/2)

    if count_dash%2!=0:
        result=(countd+1)*count_u_line*countd
    else:
        result=countd*count_u_line*countd
    print(result)