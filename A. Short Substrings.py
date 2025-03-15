t=int(input())
for _ in range(t):
    s=input()
    x=len(s)
    new_str=s[0]
    for i in range(1,x,2):
        new_str+=s[i]
        
    print(new_str)
