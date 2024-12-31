ipt=[[0,1],[0,2],[0,3],[0,4],[1,3],[2,3],[2,4],[2,5],[3,5]]
n=6
mat=[]
for i in range(n):
    temp=[]
    for j in range(n):
        temp.append(0)
        
    mat.append(temp)

for (u,v) in ipt:
    mat[u][v]=1
    mat[v][u]=1
    
for item in mat:
    print(item)