x=input()
z=input()
l='qwertyuiopasdfghjkl;zxcvbnm,./'
c=[]
if x=='R':
    for i in range(len(z)):
        for j in range(len(l)):
            if z[i]==l[j]:
                c.append(l[j-1])
elif x=='L':
    for i in range(len(z)):
        for j in range(len(l)-1):
            if z[i]==l[j]:
                c.append(l[j+1])

print("".join(c))
