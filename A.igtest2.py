grid=[]
for _ in range(4):
    grid.append(input().strip())

for i in range(3):
    for j in range(3):
        cell=[
            grid[i][j],grid[i][j+1],
            grid[i+1][j],grid[i+1][j+1]
        ]

        black_cell=cell.count('#')
        white_cell=cell.count('.')

        if black_cell>=3 or white_cell>=3:
            print("YES")
            exit()
print("NO")