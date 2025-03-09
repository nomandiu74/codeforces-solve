t = int(input())

for _ in range(t):
    n, x = map(int, input().split())
    a = []

    for i in range(n):
        if (i | x) != x:
            a = [0] * n 
            break
        a.append(i)

    curr_or = 0
    for value in a:
        curr_or |= value

    if curr_or != x:
        a.pop()
        a.append(x) 
    print(" ".join(map(str, a)))
