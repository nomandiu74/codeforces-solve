t=int(input())
while t>0:
    t-=1
    n=int(input())
    s=input()

    last_tsk=None
    sus=False
    visit=set()

    for S in s:
        if S==last_tsk:
            continue
        if S in visit:
            sus=True
            break
        visit.add(S)
        last_tsk=S

    if sus:
        print("NO")
    else:
        print("YES")

