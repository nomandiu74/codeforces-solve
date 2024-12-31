m=int(input())
for _ in range(m):
  n=int(input())
  s=input()
  
  A=s.count("A")
  B=s.count("B")
  C=s.count("C")
  D=s.count("D")
  x=min(A,n)+min(B,n)+min(C,n)+min(D,n)
  print(x)