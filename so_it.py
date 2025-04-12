matrix=[]
n=int(input("Enter the number of rows and column:"))
for i in range(n):
    arr=list(map(int,input().split()))
    matrix.append(arr)
#row addition
row_sum=[]
for row in matrix:
    row_sum.append(sum(row))
#column addition:
col_sums=[]
col_num=len(matrix[0])
for j in range(col_num):
    col_sum=0
    for i in range(n):
        col_sum+=matrix[i][j]
    col_sums.append(col_sum)
print(col_sums,row_sum)