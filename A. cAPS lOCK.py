n=input()
if len(n)==1 and n[0].islower():
    print(n.upper())
else:
    if n.isupper():
        print(n.lower())
    elif n[0].islower() and n[1:].isupper():
        print(n[0].upper()+n[1:].lower())
    else:
        print(n)

