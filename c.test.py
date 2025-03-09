<<<<<<< HEAD
n, m = map(int, input().split())

friends = list(map(str,input().split()))
p_slices = list(map(int, input().split()))

max_slice = sum(p_slices)
result = [0] * (max_slice + 1)

odd_slices = [p_slices[k] % 2 != 0 for k in range(n)]

for i in range(m):
    for j in range(i + 1, m):
        monocorp = 0
        quarrel = False

        for k in range(n):
            pizza = chr(65 + k)
            if pizza not in friends[i] and pizza not in friends[j]:
                monocorp += p_slices[k]
            elif pizza in friends[i] and pizza in friends[j]:
                if odd_slices[k]: 
                    quarrel = True
                    break

        if not quarrel:
            result[monocorp] += 1

print(" ".join(map(str, result)))
=======
n, m = map(int, input().split())

friends = list(map(str,input().split()))
p_slices = list(map(int, input().split()))

max_slice = sum(p_slices)
result = [0] * (max_slice + 1)

odd_slices = [p_slices[k] % 2 != 0 for k in range(n)]

for i in range(m):
    for j in range(i + 1, m):
        monocorp = 0
        quarrel = False

        for k in range(n):
            pizza = chr(65 + k)
            if pizza not in friends[i] and pizza not in friends[j]:
                monocorp += p_slices[k]
            elif pizza in friends[i] and pizza in friends[j]:
                if odd_slices[k]: 
                    quarrel = True
                    break

        if not quarrel:
            result[monocorp] += 1

print(" ".join(map(str, result)))
>>>>>>> 08eb3809febe6da35a2f53c953138d330244a0ba
