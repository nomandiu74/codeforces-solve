<<<<<<< HEAD
n, m = map(int, input().split())
k = list(map(int, input().split()))
s = k[0] - 1
for i in range(1, m):
    if k[i] >= k[i-1]:
        s += k[i] - k[i-1]
    else:
        s += n - (k[i-1] - k[i])
print(s)

=======
n, m = map(int, input().split())
k = list(map(int, input().split()))
s = k[0] - 1
for i in range(1, m):
    if k[i] >= k[i-1]:
        s += k[i] - k[i-1]
    else:
        s += n - (k[i-1] - k[i])
print(s)

>>>>>>> 08eb3809febe6da35a2f53c953138d330244a0ba
