t=int(input())
result=[]
for _ in range(t):
    n,m=map(int,input().split())
    matrix=[]
    for _ in range(n):
        row=list(map(int,list(input())))
        matrix.append(row)
    row_xor=[0]*n
    col_xor=[0]*m

    for i in range(n):
        for j in range(m):
            row_xor[i]^=matrix[i][j]
            col_xor[j]^=matrix[i][j]
    rowchange=0
    for x in row_xor:
        if x!=0:
            rowchange+=1
    colchange=0
    for x in col_xor:
        if x!=0:
            colchange+=1
    minchange=max(rowchange,colchange)
    result.append(minchange)

print(*result,sep="\n")