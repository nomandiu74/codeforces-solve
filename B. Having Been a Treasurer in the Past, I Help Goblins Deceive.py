<<<<<<< HEAD
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
=======
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
>>>>>>> 08eb3809febe6da35a2f53c953138d330244a0ba
    print(result)