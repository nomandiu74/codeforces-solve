n=input()
x=[]
for i in n:
    if i=='y' or i=='Y' or i=='a' or i=='A' or i=='E' or i=='e' or i=='I' or i=='i' or i=='O' or i=='o'or i=='U'or i=='u':
        continue
    x.append(i)
l=(".".join(x))
print('.'+l.lower())