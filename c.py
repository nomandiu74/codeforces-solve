t=int(input())
results=[]
for _ in range(t):
    n,k=map(int, input().split())

    teleporters=[]
    for i in range(1,n+1):

        teleport_to=(i%n)+1
        teleporters.append(teleport_to)
    results.append(" ".join(map(str,teleporters)))
for result in results:
    print(result)
