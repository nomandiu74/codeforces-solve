<<<<<<< HEAD
n,m=map(int,input().split())

friends=list(map(str,input().split()))

p_slices=list(map(int,input().split()))


max_slice=sum(p_slices)

result=[0]*(max_slice+1)


for i in range(m):
    for j in range(i+1,m):

        like1=set(friends[i])
        like2=set(friends[j])

        monocorp=0
        qurrel=False

        for k in range(n):
            pizza=chr(65+k)
            slices=p_slices[k]

            if pizza not in like1 and pizza not in like2:
                monocorp+=slices
            elif pizza in like1 and pizza in like2:
                if slices%2 !=0:
                    qurrel=True
                    break
        if not qurrel:
            result[monocorp]+=1
print(" ".join(map(str,result)))
        
=======
n,m=map(int,input().split())

friends=list(map(str,input().split()))

p_slices=list(map(int,input().split()))


max_slice=sum(p_slices)

result=[0]*(max_slice+1)


for i in range(m):
    for j in range(i+1,m):

        like1=set(friends[i])
        like2=set(friends[j])

        monocorp=0
        qurrel=False

        for k in range(n):
            pizza=chr(65+k)
            slices=p_slices[k]

            if pizza not in like1 and pizza not in like2:
                monocorp+=slices
            elif pizza in like1 and pizza in like2:
                if slices%2 !=0:
                    qurrel=True
                    break
        if not qurrel:
            result[monocorp]+=1
print(" ".join(map(str,result)))
        
>>>>>>> 08eb3809febe6da35a2f53c953138d330244a0ba
