n=int(input())
result=0
for i in range(n):
    name=input()
    if name=='Tetrahedron':
        result+=4
    elif name=='Cube':
        result+=6
    elif name=='Octahedron':
        result+=8
    elif name=='Dodecahedron':
        result+=12
    elif name=='Icosahedron':
        result+=20
print(result)