def dfs(node,parent,cat_count,c_cats):
    if cats[node]==1:
        c_cats+=1
    else:
        c_cats=0

    if c_cats>m:
        return
    
    isleaf=True
    for n in tree[node]:
        if n!=parent:
            isleaf=False

            dfs(n,node,cat_count,c_cats)
    
    if isleaf:
        global rest_count
        rest_count+=1

x,m=map(int,input().split())
cats=[0]+list(map(int,input().split()))
tree=[[] for _ in range(x+1)]

for _ in range(x-1):
    u,v=map(int,input().split())
    tree[u].append(v)
    tree[v].append(u)
rest_count=0

dfs(1,-1,0,0)
print(rest_count)