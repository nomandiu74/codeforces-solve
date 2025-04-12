n,m,a,b=map(int,input().split())

if n<=m:
    print(min(n*a,b))
else:
    extra=n%m
    full=n-extra
    total=full//m
    cost_with_extra_singles=(total*b)+(extra*a)
    cost_with_extra_multi=(total+1)*b
    cost_all_single=n*a

    print(min(cost_with_extra_singles, cost_with_extra_multi, cost_all_single))
