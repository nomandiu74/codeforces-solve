t = int(input())

results = []

for _ in range(t):

    n, m = map(int, input().split())

    matrix = []
    for _ in range(n):
        row = list(map(int, list(input())))
        matrix.append(row)

    row_xor = [0] * n
    col_xor = [0] * m


    for i in range(n):
        for j in range(m):
            row_xor[i] ^= matrix[i][j]  
            col_xor[j] ^= matrix[i][j]  
    row_changes = 0
    for x in row_xor:
        if x != 0:
            row_changes += 1
    col_changes = 0
    for x in col_xor:
        if x != 0:
            col_changes += 1
    min_changes = max(row_changes, col_changes)
    results.append(min_changes)

for result in results:
    print(result)
