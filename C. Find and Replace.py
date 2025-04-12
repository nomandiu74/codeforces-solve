t=int(input())
for _ in range(t):
    n=int(input())
    s=input()

    char_position={}
    for i in range(n):
        if s[i] not in char_position:
            char_position[s[i]]=set()
        char_position[s[i]].add(i%2) 
    valid=True
    for char, positions in char_position.items():
        if len(positions)>1:
            valid=False
            break
    if valid:
        print("YES")
    else:
        print("NO")
